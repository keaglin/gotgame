from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class Game(models.Model):
    title = models.CharField(max_length=40)
    img = models.CharField(max_length=140)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return "%s" % (self.title)

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default='1', related_name='posts', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, default='1', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.title)

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', default='1', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.content)
