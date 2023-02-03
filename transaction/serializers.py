from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'product_name', 'seller', 'buyer' , 'prod_pic', 'quantity', 'date_added']
