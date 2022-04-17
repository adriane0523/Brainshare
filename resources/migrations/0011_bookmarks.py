# Generated by Django 3.0.5 on 2020-07-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20200619_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('html_id', models.CharField(max_length=255)),
                ('post', models.ManyToManyField(to='resources.Post')),
            ],
        ),
    ]