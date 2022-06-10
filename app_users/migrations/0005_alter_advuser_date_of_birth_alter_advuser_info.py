# Generated by Django 4.0.4 on 2022-06-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_advuser_is_activated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='date_of_birth',
            field=models.DateField(blank=True, help_text='Дата рождения через "/"', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='info',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]