from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
from .models import CustomUser, Warehouse, Product
from .serializer import CustomUserSerializer, WarehouseSerializer, ProductSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if user.user_type == 'supplier':
            serializer.save()
        else:
            raise permissions.PermissionDenied("Only suppliers can update products")

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProductDeliveryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if user.user_type == 'supplier':
            serializer.save()
        else:
            raise permissions.PermissionDenied("Only suppliers can deliver products")

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProductWithdrawalViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if user.user_type == 'consumer':
            available_quantity = serializer.instance.quantity
            requested_quantity = request.data.get('quantity', 0)
            if requested_quantity <= available_quantity:
                serializer.save(quantity=available_quantity - requested_quantity)
            else:
                raise serializers.ValidationError("Requested quantity exceeds available quantity")
        else:
            raise permissions.PermissionDenied("Only consumers can withdraw products")

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
