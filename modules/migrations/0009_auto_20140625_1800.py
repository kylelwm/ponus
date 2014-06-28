# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0008_auto_20140625_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='types',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='module',
            name='prerequisite',
            field=models.CharField(null=True, blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='module',
            name='exam_duration',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='module',
            name='exam_date',
            field=models.CharField(null=True, blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='module',
            name='preclusion',
            field=models.CharField(null=True, blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
