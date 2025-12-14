from django.urls import path
from app.decorators import login_required
from app.views.usuarios import *
from app.views.usuarios.api import *

urlpatterns = [
    path("", login_required(UsuariosView.as_view()), name="usuarios"),
    path("add/", login_required(addUsuario), name="add"),
    path("listar/", login_required(listar_usuarios), name="list"),
    path("excluir/", login_required(excluir_usuario), name="del"),
    path("alterarsenha/", login_required(alterar_senha), name="change"),
]