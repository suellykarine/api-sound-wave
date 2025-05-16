from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Musica(models.Model):
    id_externo = models.CharField(max_length=255, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=255)
    duracao = models.IntegerField()

    def __str__(self):
        return self.nome


class Playlist(models.Model):
    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    musicas = models.ManyToManyField(Musica, related_name="playlists")

    def __str__(self):
        return self.nome
