# Generated by Django 3.0.6 on 2020-06-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=1200)),
                ('index', models.IntegerField()),
            ],
        ),
    ]
