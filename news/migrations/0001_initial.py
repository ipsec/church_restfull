# Generated by Django 2.0.5 on 2018-06-01 21:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('public', models.BooleanField(default=False)),
                ('starred', models.BooleanField(default=False)),
                ('published_data', models.DateTimeField(default=datetime.datetime(2018, 6, 1, 21, 56, 41, 741314, tzinfo=utc))),
                ('text', models.TextField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]