# Generated by Django 4.0.4 on 2022-04-27 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_patient'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='user.user'),
            preserve_default=False,
        ),
    ]