from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from .serializers import PaymentSerializer
from .models import Payment


class CollectsViewSet(viewsets.ModelViewSet):
    """Вьюсет донорров."""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    pagination_class = LimitOffsetPagination