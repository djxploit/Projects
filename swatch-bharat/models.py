# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4
# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=20,blank=False)
    name = models.CharField(max_length=30,blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
class session(models.Model):
    user = models.ForeignKey(user)
    token = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=False)
    def create_token(self):
        self.token=uuid4()
class Post(models.Model):
    user = models.ForeignKey(user)
    image = models.FileField(upload_to="new_photo_db")
    image_url = models.URLField()
    posted_on = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=250)
    has_liked = models.BooleanField(default=False)
    tags = models.CharField(max_length=800)
    @property
    def like_count(self):
        return len(like.objects.filter(post=self))
    @property
    def comm(self):
        return comment.objects.filter(post=self).order_by('comm_on')
class like(models.Model):
    user = models.ForeignKey(user)
    post = models.ForeignKey(Post)
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class comment(models.Model):
    user = models.ForeignKey(user)
    post = models.ForeignKey(Post)
    comm_text = models.CharField(max_length=500)
    comm_on = models.DateTimeField(auto_now_add=True)
