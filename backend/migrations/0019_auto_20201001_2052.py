# Generated by Django 3.0.3 on 2020-10-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='birthday',
            field=models.DateField(),
        ),
    ]
