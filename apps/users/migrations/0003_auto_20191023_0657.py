# Generated by Django 2.2.6 on 2019-10-23 06:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191023_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='add_time'),
        ),
    ]
