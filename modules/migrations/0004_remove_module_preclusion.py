# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_remove_module_exam_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='preclusion',
        ),
    ]
