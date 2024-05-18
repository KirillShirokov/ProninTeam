from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from payments.serializers import PaymentReadSerializer, PaymentWriteSerializer
from payments.models import Payment


class PaymentsViewSet(viewsets.ModelViewSet):
    """Вьюсет донорров."""

    serializer_class = PaymentWriteSerializer
    queryset = Payment.objects.all()
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        """Определяет класс сериализатора в зависимости от типа запроса."""
        if self.request.method == 'GET':
            return PaymentReadSerializer
        return PaymentWriteSerializer
