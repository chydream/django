# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-16 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0003_delete_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='%Y%m/product', verbose_name='主图'),
        ),
    ]
