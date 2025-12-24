from email.policy import default
from xmlrpc.client import DateTime

from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    author_rating = models.IntegerField(default=1)


class Category(models.Model):
    category_title = models.CharField(max_length=255)
    unique = True


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.BooleanField(default=False)
    news = models.BooleanField(default=True)
    published = models.DateTimeField(auto_add_now=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=1)

    def preview(self):
        return f"{self.text[:124]}..."

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    commented = models.DateTimeField(auto_add_now=True)
    comment_rating = models.IntegerField()







