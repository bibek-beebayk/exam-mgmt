# Generated by Django 5.0.3 on 2024-03-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="exam",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="description",
            field=models.TextField(),
        ),
    ]
