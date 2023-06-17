from django.contrib.auth.models import User
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


# class UserAPIList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserAPIRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


