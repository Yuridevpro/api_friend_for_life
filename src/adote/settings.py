# src/adote/settings.py
from pathlib import Path
import os
from django.contrib.messages import constants
from dotenv import load_dotenv

# Carrega variáveis de ambiente, se o arquivo .env existir
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
#  CONFIGURAÇÕES DE DESENVOLVIMENTO LOCAL
#  Este arquivo está configurado para rodar o projeto localmente por padrão.
# ==============================================================================


# src/adote/settings.py (LINHA CORRIGIDA)

# Segurança: Uma chave padrão para o ambiente de desenvolvimento/avaliação.
SECRET_KEY = 'django-insecure-uma-chave-de-desenvolvimento-qualquer'

# Modo de depuração sempre ativo em desenvolvimento
DEBUG = True

# Permite o acesso de qualquer host localmente
ALLOWED_HOSTS = ['*']


# Aplicativos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Nossos Apps
    'usuarios',
    'divulgar',
    'adotar',
    'sobre_nos',
    'perfil',
    'pagina_inicio',
    'corsheaders',      

    # Apps de Terceiros
    # 'templated_email',
    'rest_framework',
    'drf_spectacular',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'perfil.middleware.ProfileCompleteMiddleware',
]

ROOT_URLCONF = 'adote.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'adote.wsgi.application'

# --- Banco de Dados (Configuração Local com SQLite) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Validação de Senha ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internacionalização ---
LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --- Arquivos Estáticos e de Mídia (Configuração Local) ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Para o collectstatic

# Mídia (uploads) será salva localmente na pasta /media/
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# --- Configurações de E-mail (Console) ---
# Os e-mails de confirmação e reset de senha serão impressos no terminal
# onde o 'runserver' está rodando. Nenhuma configuração de SMTP é necessária.
# O link de confirmação/reset estará no terminal, basta copiá-lo e colá-lo no navegador.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- Configuração Padrão do Campo Automático ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Tags de Mensagens do Django ---
MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}

# --- Configurações do Django REST Framework e Swagger ---
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'A Friend for Life API',
    'DESCRIPTION': 'API para a plataforma de adoção de animais A Friend for Life.',
    'VERSION': '1.0.0',
}

# (Isso diz ao Django para aceitar requisições do seu servidor local e de arquivos HTML)
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    # "null", # <-- ESSENCIAL para permitir requisições de arquivos 'file://'
]