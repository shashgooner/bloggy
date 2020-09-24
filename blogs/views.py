from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from blogs.models import Post
from blogs.forms import RegisterForm, LoginForm, PostForm

User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        return index(request)
    return login(request)


@login_required
def index(request):
    posts = Post.objects.all().order_by("-date")
    paginator = Paginator(posts, 3)
    page = request.GET.get("page")

    posts = paginator.page(page)
    return render(request, "index.html", {"posts": posts})


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.error(request, "Email or Password not correct")
            return redirect("login")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            link = reverse("index") + "?page=1"
            return redirect(link)

    return render(request, "registration/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password_first")
            user = User.objects.create_user(
                username=first_name + last_name,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            user.save()
            auth_login(request, user)
            link = reverse("index") + "?page=1"
            return redirect(link)

    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def post_blog(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            link = reverse("index") + "?page=1"
            return redirect(link)
    else:
        form = PostForm()
    return render(request, "post_new.html", {"form": form})


@login_required
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "post_details.html", {"post": post})


def logout(request):
    auth_logout(request)
    return redirect("login")