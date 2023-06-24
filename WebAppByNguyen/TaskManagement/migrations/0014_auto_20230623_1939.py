# Generated by Django 3.1.3 on 2023-06-23 12:39

import TaskManagement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0013_auto_20230623_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcreation',
            name='file',
            field=models.FileField(blank=True, upload_to='upload_files', validators=[TaskManagement.models.validate_file_extension]),
        ),
    ]