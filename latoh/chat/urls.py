from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from . import views

app_name="chat"
urlpatterns = [
    path('',login_required(views.ConversationListView.as_view()), name='conversations'),
    path('conversation/<pk>/',login_required(views.ConversationDetailView.as_view()), name='messages'),
]