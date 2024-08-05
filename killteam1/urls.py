from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createkillteam, name='createkillteam'),
]