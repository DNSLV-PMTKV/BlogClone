# Generated by Django 2.1.2 on 2018-10-17 12:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20181017_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 17, 12, 55, 54, 790066, tzinfo=utc)),
        ),
    ]