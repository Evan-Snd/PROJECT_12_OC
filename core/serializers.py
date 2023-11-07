from rest_framework.serializers import ModelSerializer

from core.models import Client, Contract


class ClientSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
