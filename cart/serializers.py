from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'product', 'added_by', 'quantity', 'date_added']