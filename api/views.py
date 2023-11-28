from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser, Warehouse, Product
from .permissions import CanSupplyProduct, CanRetrieveProduct, IsSupplier, IsConsumer
from .serializer import UserSerializer, WarehouseSerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,
                          CanSupplyProduct, 
                          CanRetrieveProduct
                         ]

    @action(detail=True, 
            methods=['post'], 
            url_path='supply', 
            permission_classes=[IsSupplier]
           )
    def supply_product(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @action(detail=True,
            methods=['post'],
            url_path='retrieve',
            permission_classes=[IsConsumer]
           )
    def retrieve_product(self, request, pk=None):
        instance = self.get_object()

        serializer = self.get_serializer(instance,
                                         data=request.data, 
                                         partial=True
                                        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

