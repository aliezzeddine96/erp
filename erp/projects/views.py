from django.shortcuts import render
from .models import Projects


# Create your views here.
def projects_view(request):
    projects = Projects.objects.all()
    return render(request, 'project/project.html', {'projects': projects})
