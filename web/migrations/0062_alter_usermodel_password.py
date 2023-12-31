# Generated by Django 4.2.3 on 2023-10-07 14:19

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0061_alter_usermodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(help_text='Password must be at least 8 characters and at most 32 characters long, and can only contain English letters and numbers.', max_length=128, validators=[web.models.PasswordValidator()], verbose_name='password'),
        ),
    ]
