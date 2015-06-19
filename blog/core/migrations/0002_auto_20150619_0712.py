# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date'], 'verbose_name': 'Artigo', 'verbose_name_plural': 'Artigos'},
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 19, 7, 12, 5, 340000), verbose_name='Data', blank=True),
        ),
    ]
