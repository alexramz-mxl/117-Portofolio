from django.shortcuts import render
from .models import Project

#Create yopur views here

def projects_list_view(request):
    projects = Project.objects.all()
    return render(request, 'content/projects_list.html', {
        'projects' : projects
    })
