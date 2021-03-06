# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lite_app', '0004_auto_20150425_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999-9999999'.", regex='\\b\\d{3}-{1}\\d{7}\\b')]),
        ),
    ]
