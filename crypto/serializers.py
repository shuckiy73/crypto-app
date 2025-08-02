from rest_framework import serializers
from .models import FavoriteCrypto

class FavoriteCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCrypto
        fields = ['crypto_id', 'name', 'symbol']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        return FavoriteCrypto.objects.create(user=user, **validated_data)