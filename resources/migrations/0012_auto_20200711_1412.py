# Generated by Django 3.0.5 on 2020-07-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_bookmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Related_projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Related Project',
            },
        ),
        migrations.AlterModelOptions(
            name='bookmarks',
            options={'verbose_name': 'Boookmark'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Case Studies'},
        ),
        migrations.AlterModelOptions(
            name='resource_page',
            options={'verbose_name': 'White Paper'},
        ),
    ]
