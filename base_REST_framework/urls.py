"""base_REST_framework URL Configuration

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
from women import views
from django.urls import path, include
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'women', views.WomenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf-ath/', include('rest_framework.urls')),
    path('api/v1/women', views.WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>', views.WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>', views.WomenAPIDetailView.as_view())
]
