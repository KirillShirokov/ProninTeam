from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
