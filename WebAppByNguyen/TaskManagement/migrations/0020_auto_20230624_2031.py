# Generated by Django 3.1.3 on 2023-06-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0019_remove_document_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
