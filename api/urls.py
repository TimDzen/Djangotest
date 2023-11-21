from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, WarehouseViewSet, ProductViewSet, DeliveryViewSet, PickupViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('warehouses', WarehouseViewSet)
router.register('products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]