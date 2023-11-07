from rest_framework.serializers import ModelSerializer

from core.models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client
