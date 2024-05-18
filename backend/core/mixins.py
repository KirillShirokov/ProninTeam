from django.db import models


class PublishDateMixin:
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        blank=True,
        null=True,
    )

class ChangeDateMixin:
    change_date = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_created=True,
        auto_now=True,
        blank=True,
        null=True,
    )
