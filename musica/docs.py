# criar_playlist_view_doc = extend_schema(
#     summary="Listar e/ou Criar Playlists",
#     description="Listar todas as playlists do usuário autenticado e/ou criar uma nova playlist.",
#     responses={201: PlaylistSerializer, 200: PlaylistSerializer},
#     examples=[
#         OpenApiExample(
#             "Exemplo de Criação de Playlist", value={"nome": "Minha Playlist Favorita"}
#         )
#     ],
# )
from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema

from .serializers import PlaylistSerializer

criar_playlist_get_doc = extend_schema(
    summary="Listar Playlists",
    description="Listar todas as playlists do usuário autenticado.",
    responses={200: "Lista de playlists"},
)

criar_playlist_post_doc = extend_schema(
    summary="Criar Playlist",
    description="Criar uma nova playlist para o usuário autenticado.",
    responses={201: "Playlist criada com sucesso"},
    examples=[
        OpenApiExample(
            "Exemplo de Criação de Playlist", value={"nome": "Minha Playlist Favorita"}
        )
    ],
)


# playlist_detalhe_view_doc = extend_schema(
#     summary="Detalhes e Exclusão de Playlist",
#     description="Recuperar ou deletar uma playlist específica do usuário.",
#     parameters=[
#         OpenApiParameter(
#             name="id", description="ID da playlist", required=True, type=int
#         )
#     ],
#     responses={200: PlaylistSerializer},
# )

from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema

playlist_detalhe_get_doc = extend_schema(
    summary="Detalhes da Playlist",
    description="Recuperar uma playlist específica do usuário autenticado.",
    parameters=[
        OpenApiParameter(
            name="id", description="ID da playlist", required=True, type=int
        )
    ],
    responses={200: "Detalhes da playlist"},
)

playlist_detalhe_patch_doc = extend_schema(
    summary="Atualizar Nome da Playlist",
    description="Atualizar o nome de uma playlist específica do usuário autenticado.",
    request={"application/json": {"nome": "Novo Nome da Playlist"}},
    parameters=[
        OpenApiParameter(
            name="id", description="ID da playlist", required=True, type=int
        )
    ],
    responses={200: "Playlist atualizada com sucesso"},
)

playlist_detalhe_delete_doc = extend_schema(
    summary="Excluir Playlist",
    description="Deletar uma playlist específica do usuário autenticado.",
    parameters=[
        OpenApiParameter(
            name="id", description="ID da playlist", required=True, type=int
        )
    ],
    responses={204: "Playlist excluída com sucesso"},
)


adicionar_musica_view_doc = extend_schema(
    summary="Adicionar Música à Playlist",
    description="Adiciona uma música a uma playlist do usuário autenticado.",
    request={
        "application/json": {
            "id_externo": "12345",
            "nome": "Minha Música",
            "duracao": 300,
        }
    },
    responses={
        200: "Música adicionada à playlist com sucesso",
        400: "Erro nos parâmetros",
        404: "Playlist não encontrada",
    },
)

remover_musica_view_doc = extend_schema(
    summary="Remover Música da Playlist",
    description="Remove uma música específica de uma playlist do usuário.",
    parameters=[
        OpenApiParameter(
            name="playlist_id",
            location=OpenApiParameter.PATH,
            description="ID da playlist",
            required=True,
            type=int,
        ),
        OpenApiParameter(
            name="musica_id",
            location=OpenApiParameter.PATH,
            description="ID da música",
            required=True,
            type=int,
        ),
    ],
    responses={
        200: "Música removida da playlist com sucesso",
        400: "Música não está na playlist",
        404: "Playlist ou Música não encontrada",
    },
)
