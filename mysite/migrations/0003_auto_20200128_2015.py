# Generated by Django 2.2.4 on 2020-01-28 17:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20200119_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='arrange',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='bed',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='dishware',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='done',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='meditation',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='morning',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='work_time',
        ),
        migrations.AlterField(
            model_name='diary',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 17, 15, 58, 908717, tzinfo=utc)),
        ),
    ]