# Generated by Django 3.2.13 on 2022-06-19 18:52
import shortuuid

from django.db import migrations
from django.db import models
from django.db.models import F
from django.db.models import Value
from django.db.models.functions import Concat


def set_legacy_uuid_for_previous_orders(apps, schema_editor):
    apps.get_model('orders.Order').objects.update(slug=Concat(Value('tds-'), F('id')))


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_AcquringPercent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.CharField(
                default='',
                unique=False,
                max_length=32,
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_legacy_uuid_for_previous_orders),
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=models.CharField(db_index=True, null=False, unique=True, max_length=32, default=shortuuid.uuid),
        ),
    ]