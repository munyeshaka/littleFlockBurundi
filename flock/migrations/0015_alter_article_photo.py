# Generated by Django 4.0 on 2021-12-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flock', '0014_alter_article_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='%Y/%m/%d/'),
        ),
    ]
