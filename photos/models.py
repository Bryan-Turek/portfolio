from django.db import models

class Photo(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to='photos')
  description = models.TextField()
  
  def __unicode__(self):
    return self.title
  
  class Meta:
    ordering = ('title',)