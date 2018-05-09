# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改 时间', auto_now=True)),
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
                ('name', models.CharField(max_length=20, verbose_name='类别名称')),
                ('logo', models.CharField(max_length=100, verbose_name='图标标识')),
                ('image', models.ImageField(upload_to='category', verbose_name='类别图片')),
            ],
            options={
                'db_table': 'df_goods_category',
<<<<<<< HEAD
                'verbose_name_plural': '商品类别',
                'verbose_name': '商品类别',
=======
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改 时间', auto_now=True)),
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
                ('image', models.ImageField(upload_to='goods', verbose_name='图片')),
            ],
            options={
                'db_table': 'df_goods_image',
<<<<<<< HEAD
                'verbose_name_plural': '商品图片',
                'verbose_name': '商品图片',
=======
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('title', models.CharField(max_length=200, verbose_name='简介')),
                ('unit', models.CharField(max_length=10, verbose_name='销售单位')),
                ('price', models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('default_image', models.ImageField(upload_to='goods', verbose_name='图片')),
                ('status', models.BooleanField(default=True, verbose_name='是否上线')),
                ('category', models.ForeignKey(to='goods.GoodsCategory', verbose_name='类别')),
            ],
            options={
                'db_table': 'df_goods_sku',
                'verbose_name_plural': '商品SKU',
                'verbose_name': '商品SKU',
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改 时间', auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('title', models.CharField(max_length=200, verbose_name='简介')),
                ('unit', models.CharField(max_length=10, verbose_name='销售单位')),
                ('price', models.DecimalField(max_digits=10, verbose_name='价格', decimal_places=2)),
                ('stock', models.IntegerField(verbose_name='库存', default=0)),
                ('sales', models.IntegerField(verbose_name='销量', default=0)),
                ('default_image', models.ImageField(upload_to='goods', verbose_name='图片')),
                ('status', models.BooleanField(verbose_name='是否上线', default=True)),
                ('category', models.ForeignKey(verbose_name='类别', to='goods.GoodsCategory')),
            ],
            options={
                'db_table': 'df_goods_sku',
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            },
        ),
        migrations.CreateModel(
            name='GoodsSPU',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('desc', tinymce.models.HTMLField(default='', blank=True, verbose_name='商品描述')),
            ],
            options={
                'db_table': 'df_goods_spu',
                'verbose_name_plural': '商品',
                'verbose_name': '商品',
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改 时间', auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('desc', tinymce.models.HTMLField(verbose_name='商品描述', default='', blank=True)),
            ],
            options={
                'db_table': 'df_goods_spu',
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            },
        ),
        migrations.CreateModel(
            name='IndexCategoryGoods',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('display_type', models.SmallIntegerField(choices=[(0, '标题'), (1, '图片')], verbose_name='展示类型')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
                ('category', models.ForeignKey(to='goods.GoodsCategory', verbose_name='商品类别')),
                ('sku', models.ForeignKey(to='goods.GoodsSKU', verbose_name='商品SKU')),
            ],
            options={
                'db_table': 'df_index_category_goods',
                'verbose_name_plural': '主页分类展示商品',
                'verbose_name': '主页分类展示商品',
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改 时间', auto_now=True)),
                ('display_type', models.SmallIntegerField(verbose_name='展示类型', choices=[(0, '标题'), (1, '图片')])),
                ('index', models.SmallIntegerField(verbose_name='顺序', default=0)),
                ('category', models.ForeignKey(verbose_name='商品类别', to='goods.GoodsCategory')),
                ('sku', models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_category_goods',
                'verbose_name': '主页分类展示商品',
                'verbose_name_plural': '主页分类展示商品',
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            },
        ),
        migrations.CreateModel(
            name='IndexPromotion',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=50, verbose_name='活动名称')),
                ('url', models.CharField(max_length=100, verbose_name='活动连接')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
            ],
            options={
                'db_table': 'df_index_promotion',
                'verbose_name_plural': '主页促销活动',
                'verbose_name': '主页促销活动',
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改 时间', auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='活动名称')),
                ('url', models.CharField(max_length=100, verbose_name='活动连接')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(verbose_name='顺序', default=0)),
            ],
            options={
                'db_table': 'df_index_promotion',
                'verbose_name': '主页促销活动',
                'verbose_name_plural': '主页促销活动',
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            },
        ),
        migrations.CreateModel(
            name='IndexSlideGoods',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='顺序')),
                ('sku', models.ForeignKey(to='goods.GoodsSKU', verbose_name='商品SKU')),
            ],
            options={
                'db_table': 'df_index_slide_goods',
                'verbose_name_plural': '主页轮播商品',
                'verbose_name': '主页轮播商品',
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='修改 时间', auto_now=True)),
                ('image', models.ImageField(upload_to='banner', verbose_name='图片')),
                ('index', models.SmallIntegerField(verbose_name='顺序', default=0)),
                ('sku', models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_slide_goods',
                'verbose_name': '主页轮播商品',
                'verbose_name_plural': '主页轮播商品',
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
            },
        ),
        migrations.AddField(
            model_name='goodssku',
            name='spu',
<<<<<<< HEAD
            field=models.ForeignKey(to='goods.GoodsSPU', verbose_name='商品SPU'),
=======
            field=models.ForeignKey(verbose_name='商品SPU', to='goods.GoodsSPU'),
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
<<<<<<< HEAD
            field=models.ForeignKey(to='goods.GoodsSKU', verbose_name='商品SKU'),
=======
            field=models.ForeignKey(verbose_name='商品SKU', to='goods.GoodsSKU'),
>>>>>>> c99ace1b00b4707ae259aca0373e6e0523dae07e
        ),
    ]
