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

    def get_queryset(self):
        groupe = Group.objects.all()
        print(groupe)
        print(self.request.user)
        return super().get_queryset()


class ContractViewSet(ModelViewSet):
    permission_classes = [IsGestion]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class EventViewset(ModelViewSet):
    permission_classes = [IsSupport, IsGestion]
    queryset = Event.objects.all()
    serializer_class = EventSerializer