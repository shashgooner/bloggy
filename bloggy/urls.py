"""bloggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.contrib import admin
from blogs import views as blog_views


ADMIN_URL = "http://en.wikipedia.org/wiki/Special:RandomInCategory/Finance"

urlpatterns = [
    url(r"^admin/", RedirectView.as_view(url=ADMIN_URL, permanent=True)),
    url(r"^$", blog_views.home, name="home"),
    url(r"^register/$", blog_views.register, name="register"),
    url(r"^login/$", blog_views.login, name="login"),
    url(r"^logout/$", blog_views.logout, name="logout"),
    url(r"^post/new/$", blog_views.post_blog, name="post"),
    url(r"^home/$", blog_views.index, name="index"),
    url(
        r"^post/(?P<post_id>\d+)/$", blog_views.post_detail, name="post-detail"
    ),
    url(r"^dont_get_in/", admin.site.urls),
]
