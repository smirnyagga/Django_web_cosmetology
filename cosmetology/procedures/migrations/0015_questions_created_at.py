# Generated by Django 4.2.4 on 2023-09-26 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedures', '0014_alter_applications_options_alter_questions_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-09-26 09:00', verbose_name='Создано'),
            preserve_default=False,
        ),
    ]