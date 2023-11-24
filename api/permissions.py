from rest_framework import permissions


class IsSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'supplier'
class IsConsumer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'consumer'

class CanSupplyProduct(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'supplier'

class CanRetrieveProduct(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'consumer'

class CanRetrieveLimitedProduct(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.user_type == 'consumer' and obj.quantity >= 1
