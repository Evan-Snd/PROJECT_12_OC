from rest_framework.serializers import ModelSerializer

from core.models import Client, Contract, Event


class ClientSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
