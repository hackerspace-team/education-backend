# Generated by Django 3.2.9 on 2021-11-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studying', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='homework_accepted',
            field=models.BooleanField(default=False),
        ),
    ]