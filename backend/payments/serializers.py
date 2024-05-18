from rest_framework import serializers

from .models import Payment

class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор платежа."""
    class Meta:
        model = Payment
        fields = ('__all__')