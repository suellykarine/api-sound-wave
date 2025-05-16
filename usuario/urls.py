from django.urls import path

from .views import (
    AtualizarUsuarioView,
    DeletarUsuarioView,
    ListaUsuariosView,
    LoginUsuarioView,
    RegistrarUsuarioView,
    logout_usuario,
)

urlpatterns = [
    path("registrar/", RegistrarUsuarioView.as_view(), name="registrar_usuario"),
    path("usuarios/", ListaUsuariosView.as_view(), name="lista-usuarios"),
    path("login/", LoginUsuarioView.as_view(), name="login_usuario"),
    path("logout/", logout_usuario, name="logout_usuario"),
    path(
        "usuarios/<int:usuario_id>/",
        AtualizarUsuarioView.as_view(),
        name="usuario-update",
    ),
    path(
        "usuarios/<int:usuario_id>/",
        DeletarUsuarioView.as_view(),
        name="usuario-delete",
    ),
]
