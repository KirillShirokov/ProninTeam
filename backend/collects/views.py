from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from .serializers import CollectSerializer
from .models import Collect


class CollectsViewSet(viewsets.ModelViewSet):
    """Вьюсет коллекций."""

    serializer_class = CollectSerializer
    queryset = Collect.objects.all()
    pagination_class = LimitOffsetPagination