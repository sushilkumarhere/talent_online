# Generated by Django 4.0.2 on 2022-03-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]