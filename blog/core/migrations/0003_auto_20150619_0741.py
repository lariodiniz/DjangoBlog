# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150619_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Titulo', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 7, 41, 21, 487000), verbose_name='Data', blank=True),
        ),
    ]
