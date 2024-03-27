# Generated by Django 5.0.3 on 2024-03-27 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0007_exam_is_featured"),
        ("users", "0007_rename_faculty_student_stream"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExamAttempts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("obtained_score", models.FloatField(blank=True, null=True)),
                ("exam_data", models.JSONField()),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exam_attempts",
                        to="exam.exam",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="exam_attempts",
                        to="users.student",
                    ),
                ),
            ],
        ),
    ]
