# Generated by Django 3.0.5 on 2022-12-11 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20221210_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='text',
        ),
    ]
