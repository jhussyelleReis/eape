# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eape', '0002_auto_20170825_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]