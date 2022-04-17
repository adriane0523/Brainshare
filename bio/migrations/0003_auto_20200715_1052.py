# Generated by Django 3.0.5 on 2020-07-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_co_principal_investigators'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory_Comitee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('image', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Co_Investigators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('image', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('image', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='team_member',
        ),
        migrations.AlterField(
            model_name='co_principal_investigators',
            name='image',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='co_principal_investigators',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
