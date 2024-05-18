from django.db.transaction import atomic
from rest_framework import serializers


from collects.models import Collect, Goal
from emails.tasks import send_email_collect_create_task
from users.serializers import CustomUserSerializer


class GoalSerializer(serializers.ModelSerializer):
    """Сериализатор целей сбора."""
    class Meta:
        model = Goal
        fields = (
            'id',
            'name',
            'slug',
        )


class CollectReadSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра сбора."""
    author = CustomUserSerializer(read_only=True)
    goal = GoalSerializer(many=True, read_only=True)
    total_amount = serializers.SerializerMethodField()
    donors_count = serializers.SerializerMethodField()

    class Meta:
        model = Collect
        fields = (
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
            'total_amount',
            'donors_count',
        )


class CollectWriteSerializer(serializers.ModelSerializer):
    """Сериализатор редактирования сбора."""
    goal = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Goal.objects.all()
    )

    class Meta:
        model = Collect
        fields = (
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

    @atomic
    def create(self, validate_data):
        goal = validate_data.pop('goal')
        collect = Collect.objects.create(**validate_data)
        collect.goal.set(goal)
        send_email_collect_create_task.delay(collect.id)
        return collect

    def update(self, collect, validate_data):
        goal = validate_data.pop('goal')
        collect = super().update(collect, validate_data)
        collect.goal.set(goal)
        return collect
