import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User



#ModelSerializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')


# Serializers
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField()


#encode and decode json, model
# class UserModel:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password
# def encode():
#     model = UserModel('qwery', 'qwery@gmail.com', '1234')
#     model_sr = UserSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
# def decode():
#     stream = io.BytesIO(b'{"username":"qwery","email":"qwery@gmail.com","password":"1234"}')
#     data = JSONParser().parse(stream)
#     serializer = UserSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
