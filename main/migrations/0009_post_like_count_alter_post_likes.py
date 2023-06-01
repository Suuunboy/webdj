# Generated by Django 4.2 on 2023-05-22 22:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]