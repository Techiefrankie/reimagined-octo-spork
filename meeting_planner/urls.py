"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import permissions

from webapp.views import home
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as drf
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls

# for building documentation
TITLE = "Meeting Planner API"
DESCRIPTION = "A simple Django web app for scheduling meetings. Has both Django MTV and REST API"

drf_schema_view = drf(
    openapi.Info(
        title=TITLE,
        default_version='v1',
        description=DESCRIPTION,
        terms_of_service="https://www.meety.com/policies/terms/",
        contact=openapi.Contact(email="techiefrankie@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view = get_schema_view(title=TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('meetings/', include('meetings.urls')),
    path('rooms/', include('rooms.urls')),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=TITLE, description=DESCRIPTION)),
    path('swagger-json', drf_schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', drf_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', drf_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
