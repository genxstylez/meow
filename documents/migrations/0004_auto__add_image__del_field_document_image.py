# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'documents_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['documents.Document'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=300)),
        ))
        db.send_create_signal(u'documents', ['Image'])

        # Deleting field 'Document.image'
        db.delete_column(u'documents_document', 'image')


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'documents_image')

        # Adding field 'Document.image'
        db.add_column(u'documents_document', 'image',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=300),
                      keep_default=False)


    models = {
        u'documents.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'documents.document': {
            'Meta': {'object_name': 'Document'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'docs'", 'symmetrical': 'False', 'to': u"orm['documents.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'embed': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'href': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['providers.Provider']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'documents.image': {
            'Meta': {'object_name': 'Image'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['documents.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        },
        u'providers.provider': {
            'Meta': {'object_name': 'Provider'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_url': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['documents']