from rest_framework import serializers 
from api.models import Product,ProductProxy
class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields='__all__'

class ProductProxySerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()

    class Meta:
        model = ProductProxy
        fields = ['name','discount']

    def get_discount(self,obj):
        return obj.discounted_price()
