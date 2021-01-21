"""bike URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from bike import views as bikeviews
from wheel import views as wheelviews

bike_router = routers.DefaultRouter()
wheel_router = routers.DefaultRouter()
bike_router.register(r'bikes', bikeviews.BikeViewSet, basename='bikes')
wheel_router.register(r'front', wheelviews.FrontWheelViewSet, basename='frontwheel')
wheel_router.register(r'rear', wheelviews.RearWheelViewSet, basename='rearwheel')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(bike_router.urls)),
    path('wheels/', wheelviews.WheelList.as_view()),
    path('wheels/', include(wheel_router.urls)),
]
