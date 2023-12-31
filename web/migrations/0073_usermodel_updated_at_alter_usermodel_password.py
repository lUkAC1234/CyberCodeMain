# Generated by Django 4.2.3 on 2023-12-17 08:32

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0072_jobknowledgesmodel_jobmodel_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(help_text='Password must be at least 8 characters and at most 32 characters long, and can only contain English letters, numbers and !$@%.', max_length=128, validators=[web.models.PasswordValidator()], verbose_name='password'),
        ),
    ]
