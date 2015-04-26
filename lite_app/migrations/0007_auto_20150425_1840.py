# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lite_app', '0006_auto_20150425_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='\\b\\d{3}\\-{1}\\d{8}\\b', message="Phone number must be entered in the format: '999-9999999'.")], blank=True),
        ),
    ]
