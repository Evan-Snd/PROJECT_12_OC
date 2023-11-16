from rest_framework.serializers import ModelSerializer

from core.models import Client, Contract, Event


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'full_name',
            "email",
            "phone_number",
            "entreprise_name",
            "created_at",
            "updated_at",
            "commercial_contact"
        ]

        extra_kwargs = {
            'commercial_contact': {"read_only": True}
        }


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
        extra_kwargs = {
            'gestion_contact': {"read_only": True}
        }


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

        extra_kwargs = {
            'commercial': {"read_only": True}
        }
