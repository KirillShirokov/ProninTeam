from django.db import models
from django.core.validators import MinValueValidator

from core.constants import (
    MAX_LENGTH_NAME_GOAL,
    MAX_LENGTH_SLUG_GOAL,
    MAX_LENGTH_NAME_COLLECT,
    MAX_LENGTH_DESCRIPTION_COLLECT,
    MAX_DECIMAL_DIGITS,
    MAX_DECIMAL_PLACES,
    MIN_VALUE_VALIDATOR
)
from core.mixins import CreatedUpdatedDateModelMixin
from users.models import User


class Goal(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH_NAME_GOAL,
        unique=True,
        help_text=f'Максимальная длинна {MAX_LENGTH_NAME_GOAL} символов',
    )
    slug = models.SlugField(
        verbose_name='Уникальный слаг',
        max_length=MAX_LENGTH_SLUG_GOAL,
        unique=True,
        help_text=f'Максимальная длинна {MAX_LENGTH_SLUG_GOAL} символов',
    )

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self) -> str:
        return self.name


class Collect(CreatedUpdatedDateModelMixin):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор сбора средств',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH_NAME_COLLECT,
        help_text=f'Максимальная длинна {MAX_LENGTH_NAME_COLLECT} символов',
    )
    goal = models.ForeignKey(
        Goal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Цель сбора средств',
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=MAX_LENGTH_DESCRIPTION_COLLECT,
        help_text='Максимальная длинна'
                  f'{MAX_LENGTH_DESCRIPTION_COLLECT} символов',
    )
    total_goal = models.DecimalField(
        verbose_name='Необходимая сумма средств сбора',
        max_digits=MAX_DECIMAL_DIGITS,
        decimal_places=MAX_DECIMAL_PLACES,
        default=None,
        validators=(
            MinValueValidator(
                MIN_VALUE_VALIDATOR,
                message=(
                    f'Введите значение больше {MIN_VALUE_VALIDATOR}.'
                )
            ),
        ),
    )
    is_limited = models.BooleanField(
        verbose_name='Сбор ограничен/не ограничен',
        default=True,
    )
    image = models.ImageField(
        verbose_name='Обложка сбора',
        blank=True,
        null=True,
        upload_to='images/%Y/%m/%d',
    )
    completion_date = models.DateTimeField(
        verbose_name='Дата завершения сбора средств',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Сбор средств'
        verbose_name_plural = 'Сборы средств'
        ordering = ('-completion_date',)

    def __str__(self):
        return self.name
