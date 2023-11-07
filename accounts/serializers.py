from rest_framework.serializers import ModelSerializer

from accounts.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'password1')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        password = validated_data.pop('password', None)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
