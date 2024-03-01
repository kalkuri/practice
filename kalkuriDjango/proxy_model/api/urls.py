from api.views import ProductViewSet,ProductProxyViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'product', ProductViewSet, basename="product")
router.register(r'productproxy', ProductProxyViewSet, basename="productproxy")
urlpatterns = [
    
]+router.urls