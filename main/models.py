from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.email
    
class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title
