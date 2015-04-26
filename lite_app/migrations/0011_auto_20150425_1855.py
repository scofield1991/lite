# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('lite_app', '0010_auto_20150425_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='\\b\\d{3}-\\d{7}\\b', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], blank=True),
        ),
    ]
