# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Slideshow'
        db.create_table('slideshow_slideshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='flash', max_length=20)),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('auto_play', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('loop_play', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('random', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('display_time', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('transition_speed', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('music_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('music_loop', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('slideshow', ['Slideshow'])

        # Adding model 'SlideshowImage'
        db.create_table('slideshow_slideshowimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('slideshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slideshow.Slideshow'])),
        ))
        db.send_create_signal('slideshow', ['SlideshowImage'])


    def backwards(self, orm):
        
        # Deleting model 'Slideshow'
        db.delete_table('slideshow_slideshow')

        # Deleting model 'SlideshowImage'
        db.delete_table('slideshow_slideshowimage')


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
        }
    }

    complete_apps = ['slideshow']
