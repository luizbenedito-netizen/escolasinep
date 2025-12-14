from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/home/", permanent=False)),
    path("login/", include("app.urls.login")),
    path("home/", include("app.urls.home")),
    path("relatorios/", include("app.urls.relatorios")),
    path("usuarios/", include("app.urls.usuarios")),
]