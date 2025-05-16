from django.urls import path

from .views import (
    AdicionarMusicaPlaylistView,
    CriarPlaylistView,
    PlaylistDetalheView,
    RemoverMusicaPlaylistView,
)

urlpatterns = [
    path("playlists/", CriarPlaylistView.as_view(), name="playlist-list-create"),
    path("playlists/<int:pk>/", PlaylistDetalheView.as_view(), name="playlist-detail"),
    path(
        "playlists/<int:playlist_id>/musicas/",
        AdicionarMusicaPlaylistView.as_view(),
        name="playlist-add-musica",
    ),
    path(
        "playlists/<int:playlist_id>/musicas/<int:musica_id>/",
        RemoverMusicaPlaylistView.as_view(),
        name="playlist-remove-musica",
    ),
]
