# Generated by Django 4.2.3 on 2023-09-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_contactusmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]