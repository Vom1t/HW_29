"""HW_27 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from ads import views
from ads.views import root, AdListCreateView, CatListCreateView, CatDetailView, AdDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('ad/', AdListCreateView.as_view()),
    path('cat/', CatListCreateView.as_view()),
    path('cat/<int:pk>', CatDetailView.as_view()),
    path('ad/<int:pk>', AdDetailView.as_view()),
]
