from rest_framework import serializers

from .models import Collect

class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор сбора."""
    class Meta:
        model = Collect
        fields = ('__all__')