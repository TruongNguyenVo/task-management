# Generated by Django 3.1.3 on 2023-05-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0004_auto_20230524_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcreation',
            name='finishDate',
            field=models.DateTimeField(),
        ),
    ]
