# Generated by Django 4.0.4 on 2022-05-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_alter_setchoice_answer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setchoice',
            name='answer_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
