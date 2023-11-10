from rest_framework.routers import SimpleRouter

from core import views


router = SimpleRouter()
router.register('clients', views.ClientViewSet, basename='clients')
router.register('contracts', views.ContractViewSet, basename='contracts')
router.register('events', views.EventViewset, basename='events')

urlpatterns = router.urls
