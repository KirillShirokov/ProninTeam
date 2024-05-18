from django.contrib import admin

from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'donor',
        'collect',
        'amount',
        'pub_date',
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


admin.site.register(Payment, PaymentAdmin)
