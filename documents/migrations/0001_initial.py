# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'documents_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'documents', ['Category'])

        # Adding model 'Document'
        db.create_table(u'documents_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['providers.Provider'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('href', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=300)),
            ('views', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('embed', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'documents', ['Document'])

        # Adding M2M table for field category on 'Document'
        m2m_table_name = db.shorten_name(u'documents_document_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('document', models.ForeignKey(orm[u'documents.document'], null=False)),
            ('category', models.ForeignKey(orm[u'documents.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['document_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'documents_category')

        # Deleting model 'Document'
        db.delete_table(u'documents_document')

        # Removing M2M table for field category on 'Document'
        db.delete_table(db.shorten_name(u'documents_document_category'))


    models = {
        u'documents.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'documents.document': {
            'Meta': {'object_name': 'Document'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['documents.Category']", 'symmetrical': 'False'}),
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