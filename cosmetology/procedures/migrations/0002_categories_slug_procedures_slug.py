# Generated by Django 4.2.4 on 2023-09-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='procedures',
            name='slug',
            field=models.SlugField(max_length=200, null=True, verbose_name='URL'),
        ),
    ]