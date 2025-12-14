from django.contrib import admin
from django.urls import include, path
from app.views.errors.errors import error_404

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
]

handler404 = error_404