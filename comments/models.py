from django.db import models
from blog.models import Post

class Comment(models.Model):
    author = models.CharField(max_length=200)
    posted  = models.DateField()
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name='comments')

    def __unicode__(self):
        return self.comment

    class Meta:
        ordering = ('posted',)