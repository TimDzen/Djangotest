from rest_framework import serializers

from api.models import CustomUser, Warehouse, Product


class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'user_types')
        extra_kwargs = {'password': {'write_only': True}}


class WarehouseSerializer(serializers.Serializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = "__all__"
