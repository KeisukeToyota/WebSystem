from django.db import models
from django.contrib import admin


# class Users(models.Model):
#     id = models.CharField(primary_key=True, unique=True, max_length=255)
#     email = models.CharField(unique=True, max_length=255)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    # user = models.ForeignKey(Users)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    blog = models.ForeignKey(Blog)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

