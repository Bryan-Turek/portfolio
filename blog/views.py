from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
import re

def list(request):
    post_list = Post.objects.all()
    response = [{'id': post.id,
                 'slug': post.slug,
                 'name': post.name,
                 'posted': post.posted.strftime('%b %d, %y')} for post in post_list]
    return HttpResponse(simplejson.dumps(response) , mimetype="application/json")

def post(request, post_slug):
    post_id = re.split("-", post_slug)
    post = get_object_or_404(Post, id=post_id[0])
    cats = post.posts.all()
    try:
      if post.get_previous_by_posted():
        previousId = post.get_previous_by_posted().id
        previousSlug = '-'+post.get_previous_by_posted().slug
    except Post.DoesNotExist:
        previousId = False
        previousSlug = ''
    try:
      if post.get_next_by_posted():
        nextId = post.get_next_by_posted().id
        nextSlug = '-'+post.get_next_by_posted().slug
    except Post.DoesNotExist:
        nextId = False
        nextSlug = ''
    response = {'id': post.id,
                'previous': previousId,
                'next': nextId,
                'slug': post.slug,
                'name': post.name,
                'content': post.content,
                'posted': post.posted.strftime('%b %d, %y'),
                'comments': post.comments.all().count(),
                'featuredImage': post.featuredImage.image.url if post.featuredImage else False,
                'author': post.author.username,
                'categories': [{'name': category.name} for category in cats]}
    return HttpResponse(simplejson.dumps(response), mimetype="application/json")
  
def comments(request, post_slug):
    post_id = re.split("-", post_slug)
    post = get_object_or_404(Post, id=post_id[0])
    comments_list = post.comments.all()
    response = [{'id': comment.id,
                 'author': comment.author,
                 'comment': comment.comment,
                 'posted': comment.posted.strftime('%b %d, %y')} for comment in comments_list]
    return HttpResponse(simplejson.dumps(response) , mimetype="application/json")