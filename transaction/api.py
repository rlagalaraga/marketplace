from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from transaction import serializers
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from users import custom_permissions
from .models import Transaction

class TransactionViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.TransactionSerializer

    def get(self, *args, **kwargs):
        transact = Transaction.objects.all()
        serializer = self.serializer_class(transact, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(buyer=self.request.user)
        return Response({}, status=status.HTTP_201_CREATED)