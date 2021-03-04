"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import (
    dashboard_view,
)
from login.views import (
    login_view,
    logout_view
)
from inventory.views import (
    rawmaterials_view,
    tools_view
)
from projects.views import projects_view

admin.site.site_header = "Enterprise Resource Planning"
admin.site.site_title = "Admin - Enterprise Resource Planning"
admin.site.index_title = "Welcome to Admin - ERP portal"

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('inventory/tools/', tools_view, name='tools'),
    path('inventory/rawmaterials/', rawmaterials_view, name='rawmaterials'),
    path('projects/', projects_view, name='projects'),
    path('admin/', admin.site.urls),
]
