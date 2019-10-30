# Generated by Django 2.2.6 on 2019-10-23 06:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20191023_0616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'verbose_name': 'UserAddress', 'verbose_name_plural': 'UserAddress'},
        ),
        migrations.AlterModelOptions(
            name='userfav',
            options={'verbose_name': 'UserFav', 'verbose_name_plural': 'UserFav'},
        ),
        migrations.AlterModelOptions(
            name='userleavingmessage',
            options={'verbose_name': 'UserLeavingMessage', 'verbose_name_plural': 'UserLeavingMessage'},
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default='', max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='district',
            field=models.CharField(default='', max_length=100, verbose_name='district'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='province',
            field=models.CharField(default='', max_length=100, verbose_name='province'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='signer_mobile',
            field=models.CharField(default='', max_length=11, verbose_name='signer_mobile'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='signer_name',
            field=models.CharField(default='', max_length=100, verbose_name='signer_name'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='goods',
            field=models.ForeignKey(help_text='goods id', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='goods'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='file',
            field=models.FileField(help_text='file', upload_to='message/images/', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='message',
            field=models.TextField(default='', help_text='message context', verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='message_type',
            field=models.IntegerField(choices=[(1, 'Leave message'), (2, 'complain'), (3, 'ask for help'), (4, 'service'), (5, 'ask for goods')], default=1, help_text='MESSAGE CHOICES: 1(Leave message),2(complain),3(ask for help),4(service),5(ask for goods)', verbose_name='message_type'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='subject',
            field=models.CharField(default='', max_length=100, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]