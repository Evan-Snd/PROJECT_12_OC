from rest_framework.viewsets import ModelViewSet

from core.models import Client, Contract
from core.serializers import ClientSerializer, ContractSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
