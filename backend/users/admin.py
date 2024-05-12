from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'username',
        'first_name',
        'last_name',
        'patronymic',
    )
    list_display_links = (
        'username',
    )
    search_fields = (
        'username',
    )
    list_filter = (
        'username',
    )


admin.site.register(User, UserAdmin)
