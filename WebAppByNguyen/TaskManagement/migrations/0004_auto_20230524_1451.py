# Generated by Django 3.1.3 on 2023-05-24 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0003_auto_20230524_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcreation',
            name='finishDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='taskcreation',
            name='endDate',
            field=models.DateTimeField(),
        ),
    ]
