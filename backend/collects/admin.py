from django.contrib import admin

from .models import Collect, Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'goal',
        'description',
        'total_goal',
        'is_limited',
        'image',
        'completion_date',
        'created_at',
        'updated_at',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )
