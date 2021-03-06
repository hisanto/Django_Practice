from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title + self.author.username

class Comment(models.Model):
    email = models.EmailField(max_length=50)
    comment_text = models.CharField(max_length=200)
    comment_created_date = models.DateTimeField(auto_now_add=True)
    published_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.email