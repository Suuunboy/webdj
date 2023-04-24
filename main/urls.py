
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index),
    path('main', views.main),
    path('main/about_us/', views.about_us)
]
