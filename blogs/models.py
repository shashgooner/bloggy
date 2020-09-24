# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime as dt
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, help_text="Title of the Post")
    body = models.TextField(help_text="Content of the Post")
    date = models.DateTimeField(default=dt.datetime.now)
