from django.contrib.auth.models import User
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPI(APIView):
    def get(self, request):
        lst = User.objects.all().values()
        return Response({'users': list(lst)})

    def post(self, request):
        post_user = User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )


        return Response({'post': model_to_dict(post_user)})
