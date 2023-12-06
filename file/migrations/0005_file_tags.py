# Generated by Django 4.2.7 on 2023-11-17 06:14

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('file', '0004_alter_file_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
