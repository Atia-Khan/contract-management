# Generated by Django 4.2.7 on 2023-12-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0009_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
