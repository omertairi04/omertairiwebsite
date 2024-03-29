# Generated by Django 4.1.3 on 2023-01-11 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.posts'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.image'),
        ),
    ]
