from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from boardgames.views import add, index

urlpatterns = [
    path("index/", index, name="index"),
    path("add/", add, name="addboardgames"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
