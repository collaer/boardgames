from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from boardgames.views import index

urlpatterns = [
    path("", index, name="boardgames"),
    path("boardgames/", include("boardgames.urls")),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
