from django.urls import include, path

urlpatterns = [
    path("escolas/", include("app.urls.relatorios.escolas")),
]