# Generated by Django 3.1.3 on 2020-12-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0019_auto_20201110_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pdf_link',
        ),
        migrations.AddField(
            model_name='post',
            name='presentation_link',
            field=models.TextField(blank=True),
        ),
    ]
