# Generated by Django 3.0.3 on 2020-10-02 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_userdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='user_id',
            new_name='user',
        ),
    ]
