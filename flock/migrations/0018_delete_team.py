# Generated by Django 4.0 on 2021-12-31 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flock', '0017_alter_team_email_alter_team_full_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Team',
        ),
    ]