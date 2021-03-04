from django.shortcuts import render
from inventory.models import (
    RawMaterials,
    Tools
)
from projects.models import Projects


# Create your views here.
def dashboard_view(request):
    tools = Tools.objects.all().order_by('-id')
    materials = RawMaterials.objects.all().order_by('-id')
    projects = Projects.objects.all().order_by('-id')
    return render(request, 'dashboard/dashboard.html', {'tools': tools, 'materials': materials, 'projects': projects})
