# Generated by Django 4.0 on 2021-12-12 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sermon',
            old_name='thumb',
            new_name='photo',
        ),
    ]
