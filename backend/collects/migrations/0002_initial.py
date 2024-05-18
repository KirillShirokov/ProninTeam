# Generated by Django 4.2.13 on 2024-05-17 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор сбора средств'),
        ),
        migrations.AddField(
            model_name='collect',
            name='goal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collects.goal', verbose_name='Цель сбора средств'),
        ),
    ]
