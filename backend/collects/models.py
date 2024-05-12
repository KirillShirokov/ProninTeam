from django.db import models

from core.constants import (MAX_LENGTH_NAME_GOAL,
                            MAX_LENGTH_SLUG_GOAL,
                            MAX_LENGTH_NAME_COLLECT,
                            MAX_LENGTH_DESCRIPTION_COLLECT)
from users.models import User


class Goal(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH_NAME_GOAL,
        unique=True,
        help_text='Максимальная длинна 200 символов',
    )
    slug = models.SlugField(
        verbose_name='Уникальный слаг',
        max_length=MAX_LENGTH_SLUG_GOAL,
        unique=True,
        help_text='Максимальная длинна 200 символов',
    )

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self) -> str:
        return self.name


class Collect(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор сбора средств',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENGTH_NAME_COLLECT,
    )
    goal = models.ManyToManyField(
        Goal,
        verbose_name='Цель сбора средств',
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=MAX_LENGTH_DESCRIPTION_COLLECT,
    )
    total_goal = models.PositiveIntegerField(
        verbose_name='Необходимая сумма средств сбора'
    )
    amount_collected = models.PositiveIntegerField(
        verbose_name='Собранная сумма средств'
    )
    quantity_donors = models.PositiveIntegerField(
        verbose_name='Количество участников'
    )
    image = models.ImageField(
        verbose_name='Обложка сбора',
        blank=True,
        null=True,
        upload_to='images/%Y/%m/%d',
    )
    completion_date = pub_date = models.DateTimeField(
        auto_now_add=True,
    )    
    pub_date = models.DateTimeField(
        verbose_name='Дата завершения сбора средств',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Сбор средств'
        verbose_name_plural = 'Сборы средств'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name
