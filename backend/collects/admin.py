from django.contrib import admin

from .models import Collect, Goal


class GoalAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
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


class CollectAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'name',
        'goal',
        'description',
        'total_goal',
        'is_limited',
        'image',
        'completion_date',
        'pub_date',
        'change_date',

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

admin.site.register(Goal, GoalAdmin)
admin.site.register(Collect, CollectAdmin)
