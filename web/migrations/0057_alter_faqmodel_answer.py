# Generated by Django 4.2.3 on 2023-10-05 07:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0056_checkout_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqmodel',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
    ]