from django.contrib import admin
from .models import (
	Tools,
	RawMaterials,
)
# Register your models here.
admin.site.register(Tools)
admin.site.register(RawMaterials)
