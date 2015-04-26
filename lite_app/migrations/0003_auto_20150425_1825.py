# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lite_app', '0002_auto_20150425_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10, blank=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999-9999999'. ", regex='\x08\\d{3}-d{7}\x08')]),
        ),
    ]
