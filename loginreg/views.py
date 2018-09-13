from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# Create your views here.
class Register(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

# class Login(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('X_USERNAME')
#         if not username:
#             return None
#
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')
#
#         return (user, None)
#
# class Login(APIView):
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)