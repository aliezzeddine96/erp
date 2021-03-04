from django.shortcuts import render
from .models import (
    Tools,
    RawMaterials
)


# Create your views here.
def tools_view(request):
    tools = Tools.objects.all()
    return render(request, 'inventory/tools.html', {'tools': tools})


def rawmaterials_view(request):
    materials = RawMaterials.objects.all()
    return render(request, 'inventory/rawmaterials.html', {'materials': materials})