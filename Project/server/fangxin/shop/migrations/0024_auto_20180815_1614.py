# Generated by Django 2.0.7 on 2018-08-15 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20180815_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='limitTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 16, 14, 38, 594890), verbose_name='限时商品截止时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 15, 16, 14, 38, 590892), verbose_name='创建时间'),
        ),
    ]