from django.db import models
from django.contrib.auth.models import User

    
class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    likes = models.ManyToManyField(User, related_name='blog_post', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')

    def __str__(self):
        return self.title
    
    def num_likes(self):
        return self.likes.all().count()
    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"