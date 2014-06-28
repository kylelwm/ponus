# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('module_code', models.CharField(max_length=10)),
                ('module_title', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=50)),
                ('module_description', models.TextField()),
                ('module_credit', models.PositiveIntegerField()),
                ('workload', models.CharField(max_length=50)),
                ('preclusion', models.CharField(max_length=200)),
                ('exam_date', models.CharField(max_length=200)),
                ('exam_duration', models.CharField(max_length=50)),
                ('exam_venue', models.CharField(max_length=50)),
                ('types', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('ClassNo', models.CharField(max_length=50)),
                ('LessonType', models.CharField(max_length=50)),
                ('WeekText', models.CharField(max_length=50)),
                ('DayText', models.CharField(max_length=50)),
                ('StartTime', models.CharField(max_length=50)),
                ('EndTime', models.CharField(max_length=50)),
                ('Venue', models.CharField(max_length=50)),
                ('module', models.ForeignKey(to='modules.Module', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
