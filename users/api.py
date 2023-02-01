from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import User
from users import serializers
from django.contrib.auth import login, logout, authenticate
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from users import custom_permissions

class RegisterViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserSerializer
    
    def post(self, *args, **kwargs):    
        serializer = self.serializer_class(data=self.request.data)
        password = make_password(self.request.POST['password'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(password=password)
            # user = User.objects.create(
            #     email=serializer.validated_data['email'],
            #     first_name=serializer.validated_data['first_name'],
            #     last_name=serializer.validated_data['last_name']
            # )

            # user.set_password(serializer.validated_data['password'])
            # user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(ViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.LoginSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return Response({}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(ViewSet):
    permission_classes = (custom_permissions.IsOwnerOfObject,permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.UserSerializer
    def get(self, *args, **kwargs):
        users = User.objects.get(id=self.kwargs['id'])
        serializer = self.serializer_class(users)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, *args, **kwargs):
        users = get_object_or_404(User, id=self.kwargs['id'])
        serializer = serializers.UpdateUserSerializer(users, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)