# Generated by Django 2.2.7 on 2019-11-12 17:32

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscribed',
            field=models.BooleanField(default=False, verbose_name='Subscribed to newsletter'),
        ),
    ]