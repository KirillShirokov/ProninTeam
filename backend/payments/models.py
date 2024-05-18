from django.db import models
from django.core.validators import MinValueValidator


from core.constants import (
    MAX_DECIMAL_DIGITS,
    MAX_DECIMAL_PLACES,
    MIN_VALUE_VALIDATOR    
)
from collects.models import Collect
from core.mixins import PublishDateMixin
from users.models import User


class Payment(models.Model, PublishDateMixin):
    donor = models.ForeignKey(
        User,
        verbose_name='Произвел пожертвование',
        on_delete=models.SET_NULL,
        null=True,
    )
    collect = models.ForeignKey(
        Collect,
        verbose_name='Сбор',
        on_delete=models.SET_NULL,
        null=True,
    )
    amount = models.DecimalField(
        verbose_name='Сумма пожертвования',
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
    pub_date = models.DateTimeField(
        verbose_name='Дата платежа',
        auto_now_add=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Пожертвовавший'
        verbose_name_plural = 'Пожертвовавшие'

    def __str__(self) -> str:
        return f'{self.donor} - {self.amount} - {self.pub_date}'