# Generated by Django 4.0.4 on 2022-05-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_remove_setchoice_choose_remove_setchoice_is_right_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setchoice',
            name='answer_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
