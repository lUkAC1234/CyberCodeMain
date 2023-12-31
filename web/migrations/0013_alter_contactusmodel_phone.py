# Generated by Django 4.2.3 on 2023-09-19 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_contactusmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='phone',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+123456789012'.", regex='^\\+\\d{12}$')]),
        ),
    ]
