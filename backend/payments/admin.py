from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'donor',
        'collect',
        'amount',
        'created_at',
    )
    list_display_links = (
        'donor',
    )
    search_fields = (
        'donor',
    )
    list_filter = (
        'donor',
    )
