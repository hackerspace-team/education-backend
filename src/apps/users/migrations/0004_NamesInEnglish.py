# Generated by Django 3.1.7 on 2021-04-11 15:50

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_Django31'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name_en',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name in english'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name in english'),
        ),
    ]