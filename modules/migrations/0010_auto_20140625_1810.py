# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0009_auto_20140625_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='prerequisite',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='preclusion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
