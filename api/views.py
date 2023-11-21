from rest_framework import viewsets
from .models import CustomUser, Warehouse, Product, Delivery, Pickup
from .serializer import UserSerializer, WarehouseSerializer, ProductSerializer, DeliverySerializer, PickupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class PickupViewSet(viewsets.ModelViewSet):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
