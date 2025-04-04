# Generated by Django 4.2.20 on 2025-03-24 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("studying", "0003_add_verbose_names"),
        ("homework", "0016_QuestionDropHideCrossCheckFlag"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="study",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name="+", to="studying.study"),
        ),
    ]
