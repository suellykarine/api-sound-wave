import requests
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Musica, Playlist
from .serializers import MusicaSerializer, PlaylistSerializer


class CriarPlaylistView(ListCreateAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PlaylistDetalheView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(usuario=self.request.user)


class AdicionarMusicaPlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, playlist_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id, usuario=request.user)
        except Playlist.DoesNotExist:
            return Response({"error": "Playlist não encontrada"}, status=404)

        id_externo = request.data.get("id_externo")
        nome = request.data.get("nome")
        duracao = request.data.get("duracao")

        if not id_externo or not nome or duracao is None:
            return Response(
                {"error": "id_externo, nome e duracao são obrigatórios"},
                status=400,
            )

        musica, created = Musica.objects.get_or_create(
            id_externo=id_externo,
            defaults={"nome": nome, "duracao": duracao},
        )

        playlist.musicas.add(musica)
        playlist.save()

        return Response({"message": "Música adicionada à playlist com sucesso"})


class RemoverMusicaPlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, playlist_id, musica_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id, usuario=request.user)
        except Playlist.DoesNotExist:
            return Response(
                {"error": "Playlist não encontrada"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            musica = Musica.objects.get(id_externo=musica_id)
        except Musica.DoesNotExist:
            return Response(
                {"error": "Música não encontrada"}, status=status.HTTP_404_NOT_FOUND
            )

        if musica not in playlist.musicas.all():
            return Response(
                {"error": "Música não está na playlist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        playlist.musicas.remove(musica)
        return Response(
            {"message": "Música removida da playlist com sucesso"},
            status=status.HTTP_200_OK,
        )
