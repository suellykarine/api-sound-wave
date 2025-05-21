# 🎵 Plataforma de Musicas Streaming - Backend

API REST para gerenciamento de playlists de músicas, construída com Django e Django REST Framework.

## 📋 Funcionalidades

- CRUD de playlists
- Adição e remoção de músicas nas playlists
- Autenticação de usuários
- Testes automatizados para garantir qualidade do código

## 🛠️ Requisitos

- Python 3.10+
- Django 5.2+
- Django REST Framework

### 🗃️ Banco de Dados

- **PostgreSQL 14+**
- Configuração:
  ```ini
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME=nome_do_banco
  DB_USER=usuario
  DB_PASSWORD=senha
  DB_HOST=localhost
  DB_PORT=5432
  ```

## 📦 Instalação

1. Clone o repositório:

```bash
git clone (https://github.com/suellykarine/api-sound-wave)
cd music-streaming
```

2. Crie e ative o ambiente virtual:

```
python -m venv venv
source venv/Scripts/activate
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Rode as migrations:

```
python manage.py migrate
```

5. Rode o servidor:

```
python manage.py runserver
```

6. Para rodar os testes:

```
python manage.py test
```

## 📦 Dependências

Para rodar o projeto, você precisará instalar as seguintes dependências Python:

- asgiref==3.8.1
- attrs==25.3.0
- certifi==2025.4.26
- charset-normalizer==3.4.2
- colorama==0.4.6
- coverage==7.8.0
- Django==5.2.1
- djangorestframework==3.16.0
- djangorestframework_simplejwt==5.5.0
- drf-spectacular==0.28.0
- idna==3.10
- inflection==0.5.1
- iniconfig==2.1.0
- jsonschema==4.23.0
- jsonschema-specifications==2025.4.1
- packaging==25.0
- pluggy==1.6.0
- psycopg2-binary==2.9.10
- PyJWT==2.9.0
- pytest==8.3.5
- pytest-django==4.11.1
- PyYAML==6.0.2
- referencing==0.36.2
- requests==2.32.3
- rpds-py==0.25.0
- sqlparse==0.5.3
- tzdata==2025.2
- uritemplate==4.1.1
- urllib3==2.4.0

### 🌐 Front-End

```
Clone o repositório: https://github.com/suellykarine/music-sound-front
```

### 🔒 Autenticação

- **Tipo**: JWT (Bearer Token)
- **Header**:

```http
  Authorization: Bearer <seu_token>
```

###  📌 Endpoints

## 🎵 Playlists

📜 Listar todas as playlists

`GET /musica/playlists/`

200 OK:

```json
[
  {
    "id": 1,
    "nome": "Minhas Favoritas",
    "musicas": [1, 2]
  }
]
```

➕ Criar playlist

`POST /musica/playlists/`

#### Request Body

```json
{
  "nome": "Minha playlist"
}
```

201 Created: Sucesso

400 Bad Request: Dados inválidos

## 🔍 Detalhes da playlist

📜 Lista os detalhes de uma playlist

`GET /musica/playlists/{id}/`

200 OK

```json
{
  "id": 2,
  "nome": "Minha Playlist 2",
  "usuario": 1,
  "musicas": [
    {
      "id": 1,
      "nome": "Nome da música",
      "duracao": 180,
      "id_externo": "abc123"
    }
  ]
}
```
✏️ Atualizar nome da playlist

`PATCH /musica/playlists/{id}/`

#### Request Body

```json
{
  "nome": "Minha playlist Atualizada"
}
```

200 :

```json
{
  "id": 2,
  "nome": "Minha playlist Atualizada",
  "usuario": 1,
  "musicas": [
    {
      "id": 1,
      "nome": "Nome da música",
      "duracao": 180,
      "id_externo": "abc123"
    }
  ]
}
```

400 Bad Request: Dados inválidos

404 Not Found: ID inválido

🗑️ Excluir uma playlist

`DELETE /musica/playlists/{id}/`

204 No Content: Excluído com sucesso

404 Not Found: ID inválido

## 🎶 Músicas

➕ Adicionar música a uma playlist

`POST /musica/playlists/{playlist_id}/musicas/`

```json
{
  "id_externo": "spotify:track:5Z7ygHQo02SUrFmcgpwsKW",
  "nome": "Bohemian Rhapsody",
  "duracao": 354
}
```

200 OK:

```json
{ "message": "Música adicionada com sucesso" }
```

404 Not Found: ID inválido

➖ Remover música da playlist

`DELETE /musica/playlists/{playlist_id}/musicas/{musica_id}/`

200 OK:

```json
{ "message": "Música removida com sucesso" }
```

404 Not Found: ID inválido

## 👥  Usuários

🆕 Cria um usuário

`POST /usuario/registrar/`

#### Request Body

```json
{
  "nome": "Minha playlist"
}
```

201 Created: Sucesso

400 Bad Request: Dados inválidos

📋 Listar todos os usuários

`GET /usuario/usuarios/`

200 OK:

```json
[
  {
    "id": 8,
    "email": "testando2@example.com"
  },
  {
    "id": 3,
    "email": "testando4@example.com"
  }
]
```

✏️ Atualizar um usuário

`PATCH/usuario/usuarios/{id}/atualizar`

#### Request Body

```json
{
  "email": "testando4@example.com",
  "senha": "novasenha123"
}
```

```json
{
  "message": "Usuário atualizado com sucesso"
}
```

400 Bad Request: Dados inválidos

404 Not Found: ID inválido

🗑️ Excluir um usuário

`DELETE/usuario/usuarios/{id}/deletar/`

200 OK:

```json
{
  "message": "Usuário deletado com sucesso"
}
```

404 Not Found: ID inválido

🔐 Login

`POST/usuario/login/`

#### Request Body

```json
{
  "email": "testando4@example.com",
  "senha": "novasenha123"
}
```

200 OK:

```json
{
  "usuario": {
    "id": 1,
    "email": "testando4@example.com"
  },
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NzUxNzQwMCwiaWF0IjoxNzQ3NDMxMDAwLCJqdGkiOiI3NWU1YWIyNTUxNTA0M2Q5YjU4NzU5ZWMzNzUzMmFlOCIsInVzZXJfaWQiOjF9.ZgoAzvuOlwNJpRbMgAFTSGiUoRd-xx0sfMzoV2vcJJI",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ3NDMxMzAwLCJpYXQiOjE3NDc0MzEwMDAsImp0aSI6IjY2MDNiMTE1YWVlZTQwYjc4YmE3MDlhNjU4NjkyMjE0IiwidXNlcl9pZCI6MX0.wkXXvlADddx_OJ2Snir4KxL7DVOiTqrs5DQJYlPAxb0"
}
```

400 Bad Request: Dados inválidos

🚪 Logout
`/usuario/logout/`

```json
{
  "message": "Logout realizado com sucesso"
}
```

🔍 Teste

```
python manage.py test
```
