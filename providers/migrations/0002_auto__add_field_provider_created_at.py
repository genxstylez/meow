# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Provider.created_at'
        db.add_column(u'providers_provider', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 4, 15, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Provider.created_at'
        db.delete_column(u'providers_provider', 'created_at')


    models = {
        u'providers.provider': {
            'Meta': {'object_name': 'Provider'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['providers']