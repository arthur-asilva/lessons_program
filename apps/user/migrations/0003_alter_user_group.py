# Generated by Django 4.0.4 on 2022-04-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.IntegerField(choices=[(0, 'TERAPEUTA'), (1, 'PACIENTE'), (2, 'RESPONSÁVEL')]),
        ),
    ]
