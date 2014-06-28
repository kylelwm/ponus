# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_auto_20140625_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='exam_venue',
        ),
        migrations.RemoveField(
            model_name='module',
            name='workload',
        ),
        migrations.RemoveField(
            model_name='module',
            name='types',
        ),
        migrations.RemoveField(
            model_name='module',
            name='exam_duration',
        ),
    ]
