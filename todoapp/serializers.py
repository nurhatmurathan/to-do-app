import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User



#ModelSerializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']


# Serializers
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)

        instance.save()
        return instance

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
