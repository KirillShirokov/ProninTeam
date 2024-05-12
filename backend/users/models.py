from django.contrib.auth.models import AbstractUser
from django.db import models

from core.constants import (MAX_LENGTH_EMAIL_USER,
                           MAX_LENGTH_FIRST_NAME_USER,
                           MAX_LENGTH_LAST_NAME_USER,
                           MAX_LENGTH_PATRONYMIC_USER,
                           MAX_LENGTH_USERNAME_USER,)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
        'patronymic',
    ]

    email = models.EmailField(
        max_length=MAX_LENGTH_EMAIL_USER,
        unique=True,
        blank=False,
        null=False
    )
    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME_USER,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME_USER,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME_USER,
        blank=False,
        null=False
    )
    patronymic = models.CharField(
        max_length=MAX_LENGTH_PATRONYMIC_USER,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username
    