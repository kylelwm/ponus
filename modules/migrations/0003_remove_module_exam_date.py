# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_auto_20140625_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='exam_date',
        ),
    ]
