# Generated by Django 4.2 on 2023-05-22 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
