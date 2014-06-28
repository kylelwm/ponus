# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0007_auto_20140625_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='module_credit',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
