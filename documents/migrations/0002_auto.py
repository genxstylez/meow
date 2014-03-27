# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field category on 'Document'
        db.delete_table(db.shorten_name(u'documents_document_category'))

        # Adding M2M table for field categories on 'Document'
        m2m_table_name = db.shorten_name(u'documents_document_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm[u'documents.document'], null=False)),
            ('category', models.ForeignKey(orm[u'documents.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['document_id', 'category_id'])


    def backwards(self, orm):
        # Adding M2M table for field category on 'Document'
        m2m_table_name = db.shorten_name(u'documents_document_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm[u'documents.document'], null=False)),
            ('category', models.ForeignKey(orm[u'documents.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['document_id', 'category_id'])

        # Removing M2M table for field categories on 'Document'
        db.delete_table(db.shorten_name(u'documents_document_categories'))


    models = {
        u'documents.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'documents.document': {
            'Meta': {'object_name': 'Document'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['documents.Category']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'embed': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'href': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['providers.Provider']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'providers.provider': {
            'Meta': {'object_name': 'Provider'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['documents']