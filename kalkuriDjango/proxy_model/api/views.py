from rest_framework import viewsets
from .serializers import ProductSerializer,ProductProxySerializer
from api.models import Product,ProductProxy

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductProxyViewSet(viewsets.ModelViewSet):
    queryset = ProductProxy.objects.all()
    serializer_class = ProductProxySerializer

