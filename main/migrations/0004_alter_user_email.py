# Generated by Django 4.2 on 2023-05-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
