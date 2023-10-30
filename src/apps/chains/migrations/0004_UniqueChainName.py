# Generated by Django 3.2.12 on 2022-03-19 09:40

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('chains', '0003_LimitParentChoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AddConstraint(
            model_name='chain',
            constraint=models.UniqueConstraint(fields=('name', 'course'), name='unique_name_per_course'),
        ),
        migrations.AddConstraint(
            model_name='message',
            constraint=models.UniqueConstraint(fields=('name', 'chain'), name='unique_name_per_chain'),
        ),
    ]