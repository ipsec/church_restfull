# Generated by Django 2.0.5 on 2018-06-01 23:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180601_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_data',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 1, 23, 18, 35, 905540, tzinfo=utc)),
        ),
    ]
