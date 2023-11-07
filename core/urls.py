from rest_framework.routers import DefaultRouter

from core import views


router = DefaultRouter()
router.register('clients', views.ClientViewSet, basename='clients')

urlpatterns = router.urls
