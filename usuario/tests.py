from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Usuario


class UsuarioTests(APITestCase):
    def test_registrar_usuario_com_sucesso(self):
        url = reverse("registrar_usuario")
        data = {"email": "teste@example.com", "senha": "senha123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("usuario", response.data)
        self.assertEqual(response.data["usuario"]["email"], "teste@example.com")
        self.assertTrue(Usuario.objects.filter(email="teste@example.com").exists())

    def test_registrar_usuario_sem_email(self):
        url = reverse("registrar_usuario")
        data = {"senha": "senha123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_registrar_usuario_com_email_ja_cadastrado(self):
        Usuario.objects.create_user(email="teste@example.com", senha="senha123")
        url = reverse("registrar_usuario")
        data = {"email": "teste@example.com", "senha": "outrasenha"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
