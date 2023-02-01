from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "password", "avatar")


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "avatar")
        

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label='Email', required=True, max_length=150)
    password = serializers.CharField(label='Password')

    class Meta:
        model = User
        fields = ('email','password')

    def auth(self, request):
        auth_email = self.get('email')
        pword = self.get('password')
        return authenticate(request, email = auth_email, password = pword)