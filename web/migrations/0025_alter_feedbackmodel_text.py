# Generated by Django 4.2.3 on 2023-09-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_alter_usermodel_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='text',
            field=models.TextField(max_length=1300),
        ),
    ]