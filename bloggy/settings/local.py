import os
from bloggy.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("MYSQL_DATABASE", "blog_db"),
        "USER": os.environ.get("MYSQL_USER", "blog_root"),
        "PASSWORD": os.environ.get("MYSQL_PASSWORD", "B@pass123"),
        "HOST": "127.0.0.1",
        "OPTIONS": {"sql_mode": "STRICT_ALL_TABLES", "charset": "utf8mb4"},
    },
}
