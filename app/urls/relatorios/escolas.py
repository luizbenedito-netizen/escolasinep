from django.urls import path
from app.decorators import login_required
from app.views.relatorios.escolas import EscolasView
from app.views.relatorios.api.escolas_api import *

urlpatterns = [
    path("", login_required(EscolasView.as_view()), name="escolas"),
    # api
    path("cidades/", login_required(getCidades), name="getCidade"),
    path("estados/", login_required(getEstados), name="getEstados"),
    path("locais/", login_required(getLocais), name="getLocais"),
    path("categorias/", login_required(getCategorias), name="getCategorias"),
    path("excluir/<str:idescola>", login_required(delEscola), name="excluir")
]