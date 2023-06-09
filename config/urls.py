"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import mimetypes

import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from filebrowser.sites import site as filebrowser_site
from rest_framework import permissions, routers

from events.views import (EventsViewSet, EventTypesViewSet, EventVenuesViewSet,
                          PaidEventsViewSet, PrivateEventsViewSet)
from accounts.views import GroupsViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Event manager API snippets",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(url="https://github.com/Re-Gelu"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# REST API router
router = routers.DefaultRouter()
router.register(r'events', EventsViewSet)
router.register(r'private_events', PrivateEventsViewSet)
router.register(r'paid_events', PaidEventsViewSet)
router.register(r'event_venues', EventVenuesViewSet)
router.register(r'event_types', EventTypesViewSet)
router.register(r'groups', GroupsViewSet)    

urlpatterns = [
    
    # TinyMCE URLS
    path('tinymce/', include('tinymce.urls')),
    
    # Baton admin URLS
    path('baton/', include('baton.urls')),
    
    # Filebrowser URLS
    path('admin/filebrowser/', filebrowser_site.urls),
    
    # Admin URLS
    path('admin/', admin.site.urls),

    # Swagger URLS
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),

    # DRF URLS
    path('api/', include(router.urls)),

    # Auth URLS
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/auth/', include('djoser.urls')),

    path('api/auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
    mimetypes.add_type("application/javascript", ".js", True)
