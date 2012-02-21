# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AcceptedWord'
        db.create_table('jmbowordsuggest_acceptedword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('jmbowordsuggest', ['AcceptedWord'])

        # Adding model 'AcceptedWordCategory'
        db.create_table('jmbowordsuggest_acceptedwordcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('jmbowordsuggest', ['AcceptedWordCategory'])

        # Adding M2M table for field words on 'AcceptedWordCategory'
        db.create_table('jmbowordsuggest_acceptedwordcategory_words', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acceptedwordcategory', models.ForeignKey(orm['jmbowordsuggest.acceptedwordcategory'], null=False)),
            ('acceptedword', models.ForeignKey(orm['jmbowordsuggest.acceptedword'], null=False))
        ))
        db.create_unique('jmbowordsuggest_acceptedwordcategory_words', ['acceptedwordcategory_id', 'acceptedword_id'])


    def backwards(self, orm):
        
        # Deleting model 'AcceptedWord'
        db.delete_table('jmbowordsuggest_acceptedword')

        # Deleting model 'AcceptedWordCategory'
        db.delete_table('jmbowordsuggest_acceptedwordcategory')

        # Removing M2M table for field words on 'AcceptedWordCategory'
        db.delete_table('jmbowordsuggest_acceptedwordcategory_words')


    models = {
        'jmbowordsuggest.acceptedword': {
            'Meta': {'object_name': 'AcceptedWord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.TextField', [], {})
        },
        'jmbowordsuggest.acceptedwordcategory': {
            'Meta': {'object_name': 'AcceptedWordCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'words': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jmbowordsuggest.AcceptedWord']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['jmbowordsuggest']
