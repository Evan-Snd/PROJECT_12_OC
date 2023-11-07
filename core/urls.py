from rest_framework.routers import DefaultRouter

from core import views


router = DefaultRouter()
router.register('clients', views.ClientViewSet, basename='clients')
router.register('contracts', views.ContractViewSet, basename='contracts')

urlpatterns = router.urls
