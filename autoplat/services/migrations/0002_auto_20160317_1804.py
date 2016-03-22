# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='service_version',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_name',
            field=models.CharField(max_length=120),
        ),
    ]
