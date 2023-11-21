from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, WarehouseViewSet, ProductViewSet, DeliveryViewSet, PickupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'products', ProductViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'pickups', PickupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]