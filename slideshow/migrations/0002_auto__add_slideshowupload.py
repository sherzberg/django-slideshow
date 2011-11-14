# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SlideshowUpload'
        db.create_table('slideshow_slideshowupload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tar_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('slideshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slideshow.Slideshow'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('slideshow', ['SlideshowUpload'])


    def backwards(self, orm):
        
        # Deleting model 'SlideshowUpload'
        db.delete_table('slideshow_slideshowupload')


    models = {
        'slideshow.slideshow': {
            'Meta': {'object_name': 'Slideshow'},
            'auto_play': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'display_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loop_play': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'music_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'music_loop': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'random': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'transition_speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'flash'", 'max_length': '20'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        'slideshow.slideshowimage': {
            'Meta': {'object_name': 'SlideshowImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['slideshow.Slideshow']"})
        },
        'slideshow.slideshowupload': {
            'Meta': {'object_name': 'SlideshowUpload'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['slideshow.Slideshow']"}),
            'tar_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['slideshow']
