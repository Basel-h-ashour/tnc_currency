from rest_framework import serializers
from .models import Fiat


class FiatSerializer(serializers.ModelSerializer):
    """Serializes a Fiat object"""
    class Meta:
        model = Fiat
        fields = ('id', 'from_currency', 'to_currency', 'rate')