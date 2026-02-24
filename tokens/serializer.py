from rest_framework import serializers
from .models import Token
from users.serializer import UserSerializer

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Token
        fields = [
            'id', 'user', 'key', 'state', 'refresh_key',
            'created_at', 'expires_at', 'refreshed_at', 'revoked'
        ]