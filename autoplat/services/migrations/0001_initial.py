# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_id', models.IntegerField()),
                ('service_name', models.CharField(max_length=30)),
                ('service_port', models.IntegerField()),
                ('service_status', models.CharField(max_length=10)),
                ('remark', models.TextField()),
            ],
        ),
    ]
