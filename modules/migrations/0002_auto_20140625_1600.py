# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='module_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='exam_venue',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_credit',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='exam_duration',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='exam_date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='types',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='workload',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='preclusion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
