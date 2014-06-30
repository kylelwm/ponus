# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Module'
        db.create_table(u'modules_module', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('module_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('module_title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('module_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('module_credit', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('prerequisite', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('preclusion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('exam_date', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('exam_duration', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'modules', ['Module'])

        # Adding model 'Lesson'
        db.create_table(u'modules_lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ClassNo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('LessonType', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('WeekText', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('DayText', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('StartTime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('EndTime', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Venue', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('module', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modules.Module'])),
        ))
        db.send_create_signal(u'modules', ['Lesson'])

        # Adding model 'Semester'
        db.create_table(u'modules_semester', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('semester_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='semester', blank=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'modules', ['Semester'])

        # Adding model 'UserModule'
        db.create_table(u'modules_usermodule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('module', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modules.Module'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='usermodule', blank=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'modules', ['UserModule'])

        # Adding model 'Semester_UserModule_Link'
        db.create_table(u'modules_semester_usermodule_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usermodule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modules.UserModule'])),
            ('semester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['modules.Semester'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='link', blank=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'modules', ['Semester_UserModule_Link'])

        # Adding model 'UserProfile'
        db.create_table('user_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'modules', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'Module'
        db.delete_table(u'modules_module')

        # Deleting model 'Lesson'
        db.delete_table(u'modules_lesson')

        # Deleting model 'Semester'
        db.delete_table(u'modules_semester')

        # Deleting model 'UserModule'
        db.delete_table(u'modules_usermodule')

        # Deleting model 'Semester_UserModule_Link'
        db.delete_table(u'modules_semester_usermodule_link')

        # Deleting model 'UserProfile'
        db.delete_table('user_profile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'modules.lesson': {
            'ClassNo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'DayText': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'EndTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'LessonType': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'Lesson'},
            'StartTime': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Venue': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'WeekText': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modules.Module']"})
        },
        u'modules.module': {
            'Meta': {'object_name': 'Module'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'exam_date': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'exam_duration': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'module_credit': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'module_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'module_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'preclusion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prerequisite': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'modules.semester': {
            'Meta': {'object_name': 'Semester'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'semester'", 'blank': 'True', 'to': u"orm['auth.User']"})
        },
        u'modules.semester_usermodule_link': {
            'Meta': {'object_name': 'Semester_UserModule_Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modules.Semester']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'link'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'usermodule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modules.UserModule']"})
        },
        u'modules.usermodule': {
            'Meta': {'object_name': 'UserModule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['modules.Module']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usermodule'", 'blank': 'True', 'to': u"orm['auth.User']"})
        },
        u'modules.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'user_profile'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['modules']