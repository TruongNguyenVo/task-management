# Generated by Django 3.1.3 on 2023-06-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0020_auto_20230624_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
