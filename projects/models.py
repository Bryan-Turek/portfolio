from django.db import models
from photos.models import Photo

class Project(models.Model):
    slug = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    background = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    description = models.TextField()
    photos = models.ManyToManyField(Photo, related_name="photos")
    url = models.CharField(max_length=200)
    

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
