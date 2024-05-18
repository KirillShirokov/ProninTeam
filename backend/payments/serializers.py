from rest_framework import serializers

from emails.tasks import send_email_payment_create_task
from payments.models import Payment


class PaymentWriteSerializer(serializers.ModelSerializer):
    """Сериализатор создания платежа."""
    class Meta:
        model = Payment
        fields = (
            'id',
            'donor',
            'collect',
            'amount',
            'created_at',
        )

    def create(self, validate_data):
        payment = super().create(validate_data)
        send_email_payment_create_task.delay_on_commit(payment.id)
        return payment


class PaymentReadSerializer(serializers.ModelSerializer):
    """Сериализатор создания платежа."""
    class Meta:
        model = Payment
        fields = (
            'id',
            'donor',
            'collect',
            'amount',
            'created_at',
        )
