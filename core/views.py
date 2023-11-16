from django.contrib.auth.models import Group

from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.models import Client, Contract, Event
from core.permissions import IsCommercial, IsGestion, IsSupport
from core.serializers import (
    ClientSerializer,
    ContractSerializer,
    EventSerializer
)


class ClientViewSet(ModelViewSet):
    permission_classes = [IsCommercial]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(commercial_contact=self.request.user)


class ContractViewSet(ModelViewSet):
    permission_classes = [IsGestion]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def perform_create(self, serializer):
        serializer.save(gestion_contact=self.request.user)


class EventViewset(ModelViewSet):
    permission_classes = [IsSupport, IsGestion]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(commercial=self.request.user)
