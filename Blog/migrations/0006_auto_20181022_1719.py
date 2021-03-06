# Generated by Django 2.1.2 on 2018-10-22 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
        ('Blog', '0005_auto_20181018_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='groups.Group'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_html',
            field=models.TextField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('author', 'text')},
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
