# Generated by Django 2.1.2 on 2018-10-25 11:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0006_auto_20181022_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'text')},
        ),
    ]