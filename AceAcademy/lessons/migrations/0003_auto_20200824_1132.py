# Generated by Django 2.2.14 on 2020-08-24 03:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_lesson_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='cover',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='cover'),
        ),
    ]
