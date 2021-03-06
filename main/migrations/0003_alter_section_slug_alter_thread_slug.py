# Generated by Django 4.0.4 on 2022-06-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_thread_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='URL'),
        ),
    ]
