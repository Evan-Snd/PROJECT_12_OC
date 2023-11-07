from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from accounts.models import CustomUser
from accounts.serializers import UserSerializer


class UserViewset(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer