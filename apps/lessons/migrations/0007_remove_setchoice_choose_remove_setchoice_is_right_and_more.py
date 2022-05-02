# Generated by Django 4.0.4 on 2022-05-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_lesson_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setchoice',
            name='choose',
        ),
        migrations.RemoveField(
            model_name='setchoice',
            name='is_right',
        ),
        migrations.AddField(
            model_name='setchoice',
            name='chosen_answer',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='setchoice',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
