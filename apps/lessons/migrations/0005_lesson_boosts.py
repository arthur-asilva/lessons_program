# Generated by Django 4.0.4 on 2022-05-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_subject_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='boosts',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
