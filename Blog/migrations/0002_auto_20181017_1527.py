# Generated by Django 2.1.2 on 2018-10-17 12:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 17, 12, 27, 35, 281395, tzinfo=utc)),
        ),
    ]
