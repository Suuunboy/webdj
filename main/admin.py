from django.contrib import admin


from main.models import Post
from main.models import Like


admin.site.register(Post)
admin.site.register(Like)