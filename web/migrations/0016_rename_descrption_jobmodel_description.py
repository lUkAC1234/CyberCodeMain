# Generated by Django 4.2.3 on 2023-09-19 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_jobcategorymodel_jobmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobmodel',
            old_name='descrption',
            new_name='description',
        ),
    ]
