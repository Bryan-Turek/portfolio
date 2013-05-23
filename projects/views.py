from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render, get_object_or_404
from projects.models import Project

def list(request):
    project_list = Project.objects.all()
    response = [{'slug': project.slug,
                 'name': project.name,
                 'background': project.background,
                 'description': project.description,
                 'photos' : [{'url' : f.image.url,
                              'title' : f.title,
                              'description' : f.description} for f in project.photos.all()]} for project in project_list]
    return HttpResponse(simplejson.dumps(response) , mimetype="application/json")

def project(request, project_name):
    project = get_object_or_404(Project, slug=project_name)
    files = project.photos.all()

    response = {'name': project.name,
                'photos': [{'url': f.image.url,
                            'title': f.title,
                            'description': f.description
                            } for f in files],
                'url' : project.url,
                'industry' : project.industry,
                'background' : project.background,
                'description': project.description}
    return HttpResponse(simplejson.dumps(response), mimetype="application/json")
