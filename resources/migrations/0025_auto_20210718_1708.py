# Generated by Django 3.0.5 on 2021-07-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0024_patientstories_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientstories',
            name='picture',
            field=models.ImageField(default='none', upload_to='static/media'),
        ),
    ]