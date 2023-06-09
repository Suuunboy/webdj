# Generated by Django 4.2 on 2023-05-22 22:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_delete_post_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('likes', models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
