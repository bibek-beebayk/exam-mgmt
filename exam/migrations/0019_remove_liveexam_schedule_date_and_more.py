# Generated by Django 5.0.3 on 2024-03-28 11:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0018_remove_liveexam_end_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="liveexam",
            name="schedule_date",
        ),
        migrations.RemoveField(
            model_name="liveexam",
            name="start_time",
        ),
        migrations.AddField(
            model_name="liveexam",
            name="starts_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
