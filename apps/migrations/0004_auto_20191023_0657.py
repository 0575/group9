# Generated by Django 2.2.6 on 2019-10-23 06:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20191023_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='add_time'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='add_time'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='add_time'),
        ),
    ]