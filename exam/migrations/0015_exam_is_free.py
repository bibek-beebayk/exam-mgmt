# Generated by Django 5.0.3 on 2024-03-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0014_examattempt_time_taken"),
    ]

    operations = [
        migrations.AddField(
            model_name="exam",
            name="is_free",
            field=models.BooleanField(default=False),
        ),
    ]