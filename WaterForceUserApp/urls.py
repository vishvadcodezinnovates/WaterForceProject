"""
URL configuration for WaterForceProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import re_path,include,path
from django.views.static import serve
from WaterForceUserApp.views import *

# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static


static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
urlpatterns = [
    # path('client-slider-api/',ClientSliderApi.as_view(),name='client-slider-api'),
    # path('client-slider-api/<int:id>',ClientSliderApi.as_view(),name='client-slider-api'),
    path('client-slider-form/',client_slider_form,name='client-slider-form'),
    
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('',index,name='aksharwatertech'),
    
    path('aksharwatertech',index_page,name='aksharwatertech'),
    path('home_page',index_page,name='home_page'),
    path('about_page',about_page,name='about_page'),
    path('gallery_page',gallery_page,name='gallery_page'),
    path('services_page',services_page,name='services_page'),
    path('contact_page',contact_page,name='contact_page'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


