# Generated by Django 4.2.3 on 2023-10-03 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0051_feedbackmodel_submission_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='feedback_count',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='feedback_left',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='checkout',
        ),
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='submission_count',
        ),
    ]