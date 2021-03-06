# Generated by Django 4.0.4 on 2022-04-27 13:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('group', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
            ],
        ),
    ]
