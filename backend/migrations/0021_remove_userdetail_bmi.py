# Generated by Django 3.0.3 on 2020-10-02 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_video_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='bmi',
        ),
    ]
