from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'channel/',viewset=views.ChannelGroupViewSet)

urlpatterns = [
    path('',views.index, name='index'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('api/',include(router.urls)),
]