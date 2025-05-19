from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Usuario
from .serializers import UsuarioSerializer


class RegistrarUsuarioView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        senha = request.data.get("senha")

        if not email or not senha:
            return Response(
                {"error": "Email e senha são obrigatórios"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Usuario.objects.filter(email=email).exists():
            return Response(
                {"error": "Email já cadastrado"}, status=status.HTTP_400_BAD_REQUEST
            )

        usuario = Usuario.objects.create_user(email=email, senha=senha)
        serializer = UsuarioSerializer(usuario)
        return Response(
            {"message": "Usuário criado com sucesso", "usuario": serializer.data},
            status=status.HTTP_201_CREATED,
        )


class ListaUsuariosView(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginUsuarioView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        senha = request.data.get("senha")

        user = authenticate(request, email=email, password=senha)
        if user is None:
            return Response(
                {"error": "Credenciais inválidas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        serializer = UsuarioSerializer(user)
        return Response(
            {
                "usuario": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


@api_view(["POST"])
@permission_classes([AllowAny])
def logout_usuario(request):
    logout(request)
    return Response(
        {"message": "Logout realizado com sucesso"}, status=status.HTTP_200_OK
    )


class AtualizarUsuarioView(APIView):
    def patch(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return Response(
                {"error": "Usuário não encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

        email = request.data.get("email")
        senha = request.data.get("senha")

        if email:
            usuario.email = email

        if senha:
            usuario.set_password(senha)

        usuario.save()
        return Response(
            {"message": "Usuário atualizado com sucesso"},
            status=status.HTTP_200_OK,
        )


class DeletarUsuarioView(APIView):
    def delete(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.delete()
            return Response(
                {"message": "Usuário deletado com sucesso"},
                status=status.HTTP_200_OK,
            )
        except Usuario.DoesNotExist:
            return Response(
                {"error": "Usuário não encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )
