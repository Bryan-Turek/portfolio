from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo

class Post(models.Model):
  slug = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  content = models.TextField()
  posted = models.DateField()
  author = models.ForeignKey(User)
  featuredImage = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)
  
  def __unicode__(self):
        return self.name

  class Meta:
        ordering = ('posted',)
  
class Category(models.Model):
  name = models.CharField(max_length=200)
  posts = models.ManyToManyField(Post, related_name="posts")
  
  def __unicode__(self):
        return self.name

  class Meta:
        ordering = ('name',)