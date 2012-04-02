# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'AcceptedWord', fields ['word']
        db.create_unique('jmbowordsuggest_acceptedword', ['word'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AcceptedWord', fields ['word']
        db.delete_unique('jmbowordsuggest_acceptedword', ['word'])


    models = {
        'jmbowordsuggest.acceptedword': {
            'Meta': {'object_name': 'AcceptedWord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        'jmbowordsuggest.acceptedwordcategory': {
            'Meta': {'object_name': 'AcceptedWordCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'words': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jmbowordsuggest.AcceptedWord']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['jmbowordsuggest']
