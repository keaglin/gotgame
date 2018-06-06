from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=40)
    img = models.CharField(max_length=140)

    def __str__(self):
        return "%s" % (self.title)

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default='1', related_name='posts', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, default='1', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.title)

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', default='1', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.content)
