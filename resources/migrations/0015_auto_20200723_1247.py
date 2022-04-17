# Generated by Django 3.0.5 on 2020-07-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0014_auto_20200714_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='publications',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publications',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='publications',
            name='published_date',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='publications',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]