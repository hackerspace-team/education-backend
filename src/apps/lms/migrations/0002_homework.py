# Generated by Django 4.2.20 on 2025-03-27 07:06

from typing import no_type_check

import django.db.models.deletion
from django.db import migrations, models


@no_type_check
def create_lesson_for_each_homework_question(apps, schema_editor):  # noqa: ARG001
    Lesson = apps.get_model("lms.Lesson")
    Question = apps.get_model("homework.Question")

    for question in Question.objects.all():
        for course in question.courses.all():
            Lesson.objects.create(
                name=question.name,
                course=course,
                question=question,
                hidden=False,
            )


@no_type_check
def fix_homework_lessons_position(apps, schema_editor):  # noqa: ARG001
    Course = apps.get_model("products.Course")
    for course in Course.objects.all():
        lessons_with_materials = course.lessons.filter(question__isnull=False)
        if not lessons_with_materials.count():
            continue

        position = 1
        for lesson in list(lessons_with_materials.order_by("question__created").all()):
            lesson.update(position=position)
            lesson.save(update_fields=["position"])
            position += 1


class Migration(migrations.Migration):
    dependencies = [
        ("homework", "0018_answer_relations_fix"),
        ("lms", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL("SET CONSTRAINTS ALL IMMEDIATE"),
        migrations.AddField(
            model_name="lesson",
            name="question",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name="+", to="homework.question", verbose_name="Question"
            ),
        ),
        migrations.RunPython(create_lesson_for_each_homework_question),
        migrations.RunPython(fix_homework_lessons_position),
    ]
