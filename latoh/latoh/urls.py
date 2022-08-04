"""latoh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from chat import views as ChatViews
from rest_framework.authtoken import views as AuthTOkenViews
from .views import CustomAuthToken
from meet.views import MeetViewset
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

api_routes = routers.DefaultRouter()
api_routes.register(r'chat/users', ChatViews.UserViewset)
api_routes.register(r'chat/groups', ChatViews.GroupViewset)
api_routes.register(r'chat/messages', ChatViews.ChatViewset)
api_routes.register(r'meet', MeetViewset)

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/', include(api_routes.urls)),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
