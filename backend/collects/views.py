from django.db.models import Sum, Count
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from collects.serializers import CollectReadSerializer, CollectWriteSerializer
from collects.models import Collect
from core.permissions import IsAdminOrAuthorOrReadOnly


class CollectsViewSet(viewsets.ModelViewSet):
    """Вьюсет коллекций."""

    serializer_class = CollectReadSerializer
    queryset = Collect.objects.order_by('-created_at').annotate(
        total_amount=Sum('payments__amount'),
        donors_count=Count('payments__id', distinct=True),
    )
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminOrAuthorOrReadOnly)

    def get_serializer_class(self):
        """Определяет класс сериализатора в зависимости от типа запроса."""
        if self.request.method == 'GET':
            return CollectReadSerializer
        return CollectWriteSerializer
