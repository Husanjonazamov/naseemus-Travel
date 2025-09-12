"""
All urls configurations tree
"""

from config.env import env
from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

from django.http import HttpResponse

def home(request):
    return HttpResponse("OK")

################
# My apps url
################
urlpatterns = [
    path("", include("core.apps.accounts.urls")),
    path("health/", home),
    path("api/", include("core.apps.api.urls")),
    
]


################
# Library urls
################
urlpatterns += [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    
    
]

################
# Project env debug mode
################
if env.bool("SILK_ENEBLED", False):
    urlpatterns += [
        path('silk/', include('silk.urls', namespace='silk'))
    ]
if env.str("PROJECT_ENV") == "debug":

    ################
    # Swagger urls
    ################
    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]

################
# Media urls
################
urlpatterns += [
    re_path(r"static/(?P<path>.*)", serve, {"document_root": settings.STATIC_ROOT}),
    re_path(r"media/(?P<path>.*)", serve, {"document_root": settings.MEDIA_ROOT}),
]
