from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from cart import serializers
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from users import custom_permissions
from .models import Cart


class CartViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CartSerializer

    def get(self, *args, **kwargs):
        cart = Cart.objects.all()
        serializer = self.serializer_class(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(added_by=self.request.user)
        return Response({}, status=status.HTTP_201_CREATED)

    def delete(self, *args, **kwargs):
        cart = get_object_or_404(Cart, id=self.kwargs['id'])
        cart.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, *args, **kwargs):
        cart = Cart.objects.get(id=self.kwargs['id'])
        serializer = self.serializer_class(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put (self, *args, **kwargs):
        cart = get_object_or_404(Cart, id=self.kwargs['id'])
        serializer = self.serializer_class(cart, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)