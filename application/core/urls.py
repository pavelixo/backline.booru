from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from pages.views import RootView
from authentication.urls import urlpatterns as authentication_urlpatterns

urlpatterns = [
    path("", RootView.as_view(), name="root-view"),
    path("admin/", admin.site.urls),
    *authentication_urlpatterns,
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )