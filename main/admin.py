from django.contrib import admin

from main.models import User
from main.models import Post

# Register your models here.
admin.site.register(User)
admin.site.register(Post)