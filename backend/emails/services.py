import os

from dotenv import load_dotenv

from collects.models import Collect
from payments.models import Payment


load_dotenv(
    dotenv_path='./docker/envfiles/.env'
)


def collect_created_email(collect_id):
    collect = Collect.objects.get(pk=collect_id)
    subject = f'Информация о сборе {collect_id}.'
    message = (
        f'Сбор {collect.title} №{collect_id} успешно создан!'
    )
    sender = os.getenv('EMAIL_HOST_USER')
    recipient_list = [collect.author.email]
    message = [subject, message, sender, recipient_list]
    return message


def payment_created_email(payment_id):
    payment = Payment.objects.get(pk=payment_id)
    subject = f'Информация о платеже {payment_id}.'
    message = (
        f' Платеж {payment.collect.name} успешно создан! '
    )
    sender = os.getenv('EMAIL_HOST_USER')
    recipient_list = [payment.donor.email]
    message = [subject, message, sender, recipient_list]
    return message
