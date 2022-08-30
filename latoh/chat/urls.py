from django.urls import path, include
from rest_framework import routers
from . import views

app_name="chat"
urlpatterns = [
    path('',views.ConversationListView.as_view(), name='conversations'),
    path('conversation/<pk>/',views.ConversationDetailView.as_view(), name='messages'),
]