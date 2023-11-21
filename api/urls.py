from rest_framework.routers import DefaultRouter

from api.views import CustomUserViewSet, WarehouseViewSet, ProductViewSet, ProductDeliveryViewSet, \
    ProductWithdrawalViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('warehouse', WarehouseViewSet)
router.register('product', ProductViewSet)
router.register('ProductDelivery', ProductDeliveryViewSet)
router.register('ProductDelivery', ProductWithdrawalViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)
