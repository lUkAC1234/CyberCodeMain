# Generated by Django 4.2.3 on 2023-09-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_usermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='mobileNumber',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
