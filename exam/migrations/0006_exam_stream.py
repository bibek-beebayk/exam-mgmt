# Generated by Django 5.0.3 on 2024-03-23 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0005_alter_exam_file"),
        ("users", "0007_rename_faculty_student_stream"),
    ]

    operations = [
        migrations.AddField(
            model_name="exam",
            name="stream",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="exams",
                to="users.stream",
            ),
            preserve_default=False,
        ),
    ]
