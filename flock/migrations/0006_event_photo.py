# Generated by Django 4.0 on 2021-12-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flock', '0005_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='%Y/%m/%d/'),
        ),
    ]
