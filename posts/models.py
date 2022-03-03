from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    blog_content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=60, default=True)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
