# Plataforma de Musicas Streaming - Backend

## Descrição

API REST para gerenciamento de playlists de músicas, construída com Django e Django REST Framework.

## Funcionalidades

- CRUD de playlists
- Adição e remoção de músicas nas playlists
- Autenticação de usuários
- Testes automatizados para garantir qualidade do código

## Requisitos

- Python 3.10+
- Django 5.2+
- Django REST Framework

## Como rodar o projeto localmente

1. Clone o repositório:

```bash
git clone (https://github.com/suellykarine/streaming-music)
cd music-streaming
```

2. Crie e ative o ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
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

7. Documentação:

```
http://localhost:8000/api/docs/ — UI Swagger
```

## Dependências

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
