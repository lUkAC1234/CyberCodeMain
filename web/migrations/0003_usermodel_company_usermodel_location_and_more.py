# Generated by Django 4.2.3 on 2023-09-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_postmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='company',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='mobileNumber',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='socialMedia',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_image',
            field=models.ImageField(default='profile.svg', upload_to=' users/profile/profile-image/%Y/%m/%d/'),
        ),
    ]
