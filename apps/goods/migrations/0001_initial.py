# Generated by Django 2.2.6 on 2019-10-31 16:20

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='goods_sn')),
                ('name', models.CharField(max_length=100, verbose_name='goods_name')),
                ('click_num', models.IntegerField(default=0, verbose_name='click_num')),
                ('sold_num', models.IntegerField(default=0, verbose_name='sold_num')),
                ('fav_num', models.IntegerField(default=0, verbose_name='fav_num')),
                ('goods_num', models.IntegerField(default=0, verbose_name='goods_num')),
                ('market_price', models.FloatField(default=0, verbose_name='market_price')),
                ('shop_price', models.FloatField(default=0, verbose_name='shop_price')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='goods_brief')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='goods_desc')),
                ('ship_free', models.BooleanField(default=True, verbose_name='ship_free')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='goods_front_image')),
                ('is_new', models.BooleanField(default=False, verbose_name='is_new')),
                ('is_hot', models.BooleanField(default=False, verbose_name='is_hot')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'Goods',
                'verbose_name_plural': 'Goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='category name', max_length=30, verbose_name='category_name')),
                ('code', models.CharField(default='', help_text='category code', max_length=30, verbose_name='category_code')),
                ('desc', models.TextField(default='', help_text='category description', verbose_name='category_description')),
                ('category_type', models.IntegerField(choices=[(1, 'type 1'), (2, 'type 2'), (3, 'type 3')], help_text='category type', verbose_name='category_type')),
                ('is_tab', models.BooleanField(default=False, help_text='is tab', verbose_name='is_tab')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('parent_category', models.ForeignKey(blank=True, help_text='parent category', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='parent_category')),
            ],
            options={
                'verbose_name': 'GoodsCategory',
                'verbose_name_plural': 'GoodsCategory',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='keywords')),
                ('index', models.IntegerField(default=0, verbose_name='index')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'HotSearchWords',
                'verbose_name_plural': 'HotSearchWords',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='goods_category')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods')),
            ],
            options={
                'verbose_name': 'IndexAd',
                'verbose_name_plural': 'IndexAd',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.Goods', verbose_name='goods')),
            ],
            options={
                'verbose_name': 'GoodsImage',
                'verbose_name_plural': 'GoodsImage',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='brand name', max_length=30, verbose_name='brand_name')),
                ('desc', models.TextField(default='', help_text='brand description', max_length=200, verbose_name='brand_description')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目')),
            ],
            options={
                'verbose_name': 'GoodsCategoryBrand',
                'verbose_name_plural': 'GoodsCategoryBrand',
                'db_table': 'goods_goodsbrand',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='goods_category'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner', verbose_name='image')),
                ('index', models.IntegerField(default=0, verbose_name='index')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='goods')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
            },
        ),
    ]
