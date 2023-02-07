from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    status_name = serializers.CharField(source='get_status_display', required=False)
    category_name = serializers.CharField(source='get_category_display', required=False)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'status', 'category', 'prod_pic', 'owner', 'status_name', 'category_name', 'price', 'stock']
        read_only_fields = ['status_name', 'category_name']

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['owner'] = instance.owner.first_name + ' ' + instance.owner.last_name + '/' + str(instance.owner.id)

        return response