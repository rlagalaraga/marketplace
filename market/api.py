from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from market import serializers
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from users import custom_permissions
from .models import Product

class ProductViewSet(viewsets.ViewSet):

    permission_classes = (custom_permissions.IsOwnerOfObject,permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.ProductSerializer

    def get_all(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_owned(self, *args, **kwargs):
        serializer = self.serializer_class(
            instance=Product.objects.filter(owner=self.request.user),
            many=True,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, *args, **kwargs):
        wishlisted = False
        product = Product.objects.get(id=self.kwargs['id'])
        if product.wishlist.filter(id = self.request.user.id).exists():
            wishlisted = True
        serializer = self.serializer_class(product)
        return Response({'data': serializer.data, 'wishlisted': wishlisted}, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=self.request.user)
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs['id'])
        serializer = self.serializer_class(product, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        product = get_object_or_404(id=self.kwargs['id'])
        product.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def wishlist_product(self, *args, **kwargs):
        #import pdb; pdb.set_trace()
        product = Product.objects.get(id=self.kwargs.get("id"))
        
        if product.wishlist.filter(id = self.request.user.id).exists():
            product.wishlist.remove(self.request.user)

        else:
            product.wishlist.add(self.request.user)
        return Response({}, status=status.HTTP_200_OK)