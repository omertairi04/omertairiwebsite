# Generated by Django 4.1.3 on 2023-01-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='background_image',
        ),
    ]
