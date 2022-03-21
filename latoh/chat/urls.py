from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('room/<str:room_name>/', views.room, name='room')
]