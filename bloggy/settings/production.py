from bloggy.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ["django.notmuchstuff.com", "139.59.18.211"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "blogs",
        "USER": "shashwat",
        "PASSWORD": os.environ.get("DJANGO_DB_PASSWORD", None),
        "HOST": "blog-db-do-user-8042349-0.b.db.ondigitalocean.com",
        "PORT": "25060",
    },
}
