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
from django.conf.urls.static import static

from django.conf import settings

from rest_framework import permissions

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


from WaterForceUserApp.views import *

# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Pastebin API')

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Akshar Water Force Api",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@yourapi.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

admin.site.site_header = "AksharWaterTech Admin"
admin.site.site_title = "AksharWaterTech Admin Portal"
admin.site.index_title = "Welcome to AksharWaterTech"

static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
urlpatterns = [
    path('aksharwatertech-admin', admin.site.urls),
    # path('akshar-watertech-admin/', admin.site.urls),
    path("", include(static_urlpatterns)),
    # path('waterforce-api/', include('WaterForceUserApp.urls')),
    # path('akshar-watertech-swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='akshar-watertech-schema-swagger-ui'),
    # path('akshar-watertech-redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='akshar-watertech-schema-redoc'),
    # path('akshar-watertech-swagger.json', schema_view.without_ui(cache_timeout=0), name='akshar-watertech-schema-json'),
    
    path('',index_page,name='aksharwatertech'),
    path('aksharwatertech',index_page,name='aksharwatertech'),
    path('aksharwatertech/', include('WaterForceUserApp.urls')),
    
    
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),

]
handler404 = error_404
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)