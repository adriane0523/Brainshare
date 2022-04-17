# Generated by Django 3.0.5 on 2020-07-14 18:29

import ckeditor_uploader.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_publications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aim1',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('pdf_link', models.CharField(blank=True, max_length=500)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Aim 1',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Case Studie'},
        ),
        migrations.AlterModelOptions(
            name='publications',
            options={'verbose_name': 'Publication'},
        ),
    ]
