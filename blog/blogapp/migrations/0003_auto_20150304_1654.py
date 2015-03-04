# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20150304_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='upd_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
