from rest_framework import serializers

from .models import Musica, Playlist


class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = [
            "id",
            "nome",
            "duracao",
            "id_externo",
        ]
        read_only_fields = ["id"]


class PlaylistSerializer(serializers.ModelSerializer):
    musicas = MusicaSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ["id", "nome", "usuario", "musicas"]
        read_only_fields = ["id", "usuario"]
