# Generated by Django 2.0.6 on 2018-06-13 10:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 10, 46, 31, 946951, tzinfo=utc)),
        ),
    ]
