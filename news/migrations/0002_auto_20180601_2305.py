# Generated by Django 2.0.5 on 2018-06-01 23:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='published_data',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 1, 23, 5, 46, 400471, tzinfo=utc)),
        ),
    ]