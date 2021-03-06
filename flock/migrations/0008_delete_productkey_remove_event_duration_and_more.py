# Generated by Django 4.0 on 2021-12-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flock', '0007_productkey'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductKey',
        ),
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='event',
            name='in_progress',
        ),
        migrations.AddField(
            model_name='event',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
