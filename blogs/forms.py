from django import forms
from django.contrib.auth import get_user_model
from trix.widgets import TrixEditor
from blogs.models import Post

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")
        widgets = {
            "body": TrixEditor,
        }


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(label="Email-Id")
    password_first = forms.CharField(label="Password")
    password_again = forms.CharField(label="Confirm password")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["password_first"].widget = forms.PasswordInput()
        self.fields["password_again"].widget = forms.PasswordInput()

    def clean(self):
        cleaned_data = self.cleaned_data
        password_one = self.cleaned_data.get("password_first")
        password_two = self.cleaned_data.get("password_again")
        if password_one != password_two:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def clean_email(self):
        email_address = self.cleaned_data.get("email")
        user = User.objects.filter(email=email_address)
        if user.exists():
            raise forms.ValidationError(
                "The email address you've chosen is already registered."
            )
        return email_address
