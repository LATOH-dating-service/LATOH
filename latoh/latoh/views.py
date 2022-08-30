from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from chat.serializers import UserMSerializer
from django.views.generic import TemplateView

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwarg):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        userSerialized = UserMSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': userSerialized.data
        })

class HomeViewset(TemplateView):
    template_name: str = "base.html"