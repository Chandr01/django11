# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20171212_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customr_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=100, null=True),
        ),
    ]