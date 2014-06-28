# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0010_auto_20140625_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='types',
        ),
    ]
