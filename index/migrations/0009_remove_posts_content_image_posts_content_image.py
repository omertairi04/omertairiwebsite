# Generated by Django 4.1.3 on 2023-01-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_remove_image_project_image_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='content_image',
        ),
        migrations.AddField(
            model_name='posts',
            name='content_image',
            field=models.ManyToManyField(blank=True, null=True, to='index.image'),
        ),
    ]