from django.db import models

from collects.models import Collect
from users.models import User


class Payment(models.Model):
    donor = models.ForeignKey(
        User,
        verbose_name='Произвел пожертвование',
        on_delete=models.CASCADE,
    )
    collect = models.ForeignKey(
        Collect,
        verbose_name='Сбор',
        on_delete=models.CASCADE,
    )
    amount = models.PositiveIntegerField(
        verbose_name='Сумма пожертвования',
    )
    date_donate = models.DateTimeField(
        verbose_name='Дата пожертвования',
        auto_created=True,
    )

    class Meta:
        verbose_name = 'Пожертвовавший'
        verbose_name_plural = 'Пожертвовавшие'

    def __str__(self) -> str:
        return self.name