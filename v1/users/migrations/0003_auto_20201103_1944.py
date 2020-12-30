# Generated by Django 3.1.1 on 2020-11-03 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_userearnings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userearnings',
            options={'default_related_name': 'user_earnings', 'verbose_name_plural': 'user earnings'},
        ),
        migrations.AlterField(
            model_name='userearnings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_earnings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='userearnings',
            constraint=models.UniqueConstraint(fields=('repository', 'time_period'), name='unique_repository_time_period'),
        ),
    ]
