# Generated by Django 3.0.5 on 2020-08-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_auto_20200826_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sulton_links',
            name='link',
            field=models.TextField(blank=True),
        ),
    ]