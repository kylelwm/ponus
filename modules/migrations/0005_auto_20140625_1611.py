# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_remove_module_preclusion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='exam_duration',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_credit',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_title',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='module',
            name='department',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_code',
            field=models.CharField(blank=True, null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='exam_venue',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='module',
            name='types',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='module',
            name='workload',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]
