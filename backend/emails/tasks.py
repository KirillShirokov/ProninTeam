from celery import shared_task
from django.core.mail import send_mail

from services import collect_created_email, payment_created_email


@shared_task
def send_email_collect_create_task(collect_id):
    message = collect_created_email(collect_id)
    return send_mail(*message, fail_silently=True)


@shared_task
def send_email_payment_create_task(payment_id):
    message = payment_created_email(payment_id)
    return send_mail(*message, fail_silently=True)
