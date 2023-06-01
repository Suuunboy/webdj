
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index),
    path('login', views.log_in),
    path('main', views.main),
    path('main/about_us/', views.about_us),
    path('main/post/', views.new_post),
    path('liked/', views.like_unlike_post, name='like-post-view'),
]
