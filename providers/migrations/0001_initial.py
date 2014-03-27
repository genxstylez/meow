# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Provider'
        db.create_table(u'providers_provider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=100)),
            ('codename', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'providers', ['Provider'])


    def backwards(self, orm):
        # Deleting model 'Provider'
        db.delete_table(u'providers_provider')


    models = {
        u'providers.provider': {
            'Meta': {'object_name': 'Provider'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['providers']