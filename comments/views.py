from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render, get_object_or_404
from comments.models import Comment
from blog.models import Post
import re

def list(request):
    comments_list = Comment.objects.all()
    response = [{'id': comment.id,
                 'author': comment.author,
                 'comment': comment.comment,
                 'posted': comment.posted.strftime('%b %d, %y')} for comment in comments_list]
    return HttpResponse(simplejson.dumps(response) , mimetype="application/json")