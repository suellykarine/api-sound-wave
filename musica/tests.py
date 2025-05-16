from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Musica, Playlist

User = get_user_model()


class MusicaPlaylistTests(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(email="user@example.com", senha="senha123")
        self.client.force_authenticate(user=self.user)

        self.playlist = Playlist.objects.create(
            nome="Minha Playlist", usuario=self.user
        )

    def test_criar_playlist(self):
        url = reverse("playlist-list-create")
        data = {"nome": "Nova Playlist"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], "Nova Playlist")
        self.assertEqual(response.data["usuario"], self.user.id)
        self.assertTrue(
            Playlist.objects.filter(nome="Nova Playlist", usuario=self.user).exists()
        )

    def test_adicionar_musica_na_playlist(self):
        url = reverse("playlist-add-musica", kwargs={"playlist_id": self.playlist.id})
        data = {
            "id_externo": "abc123",
            "nome": "Música Teste",
            "duracao": 180,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)
        self.assertEqual(
            response.data["message"], "Música adicionada à playlist com sucesso"
        )

        musica = Musica.objects.get(id_externo="abc123")
        self.assertIn(musica, self.playlist.musicas.all())

    def test_remover_musica_da_playlist(self):

        musica = Musica.objects.create(
            id_externo="xyz789", nome="Música Remover", duracao=200
        )
        self.playlist.musicas.add(musica)

        url = reverse(
            "playlist-remove-musica",
            kwargs={"playlist_id": self.playlist.id, "musica_id": musica.id},
        )

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)
        self.assertEqual(
            response.data["message"], "Música removida da playlist com sucesso"
        )
        self.assertNotIn(musica, self.playlist.musicas.all())

    def test_remover_musica_que_nao_esta_na_playlist(self):
        musica = Musica.objects.create(
            id_externo="not_in_playlist", nome="Outra Música", duracao=100
        )
        url = reverse(
            "playlist-remove-musica",
            kwargs={"playlist_id": self.playlist.id, "musica_id": musica.id},
        )

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"], "Música não está na playlist")

    def test_adicionar_musica_com_dados_faltando(self):
        url = reverse("playlist-add-musica", kwargs={"playlist_id": self.playlist.id})
        data = {
            "id_externo": "abc123",
            "nome": "",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
