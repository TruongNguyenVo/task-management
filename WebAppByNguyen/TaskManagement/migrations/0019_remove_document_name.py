# Generated by Django 3.1.3 on 2023-06-24 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0018_auto_20230624_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
    ]
