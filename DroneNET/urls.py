"""DroneNET URL Configuration

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
from apps.dashboard.views import home_screen
from apps.droneManager.views import drone, drone_data, overview, s_map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen),
    path('drone/<str:id>', drone),
    path('overview/', overview),
    path('drone-data/<str:id>', drone_data),
    path('map/', s_map)
]
