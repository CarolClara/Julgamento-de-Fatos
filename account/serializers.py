from account.models import User
from rest_framework import serializers


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password')
