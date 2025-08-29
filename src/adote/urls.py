from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Importações para a API e Documentação
from divulgar.views import PetListAPIView, PetDetailAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # URLs da Aplicação Web
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('divulgar/', include('divulgar.urls')),
    path('adotar/', include('adotar.urls')),
    path('perfil/', include('perfil.urls')),
    path('sobre_nos/', include('sobre_nos.urls')),
    path('pagina_inicio/', include('pagina_inicio.urls')),
    path('', RedirectView.as_view(url='/pagina_inicio/', permanent=False)),  # Redireciona a raiz para a página inicial

    # --- URLs DA API REST ---
    path('api/pets/', PetListAPIView.as_view(), name='api_pet_list'),
    path('api/pets/<int:pk>/', PetDetailAPIView.as_view(), name='api_pet_detail'),
    
    # --- URLs DA DOCUMENTAÇÃO DA API (SWAGGER/OPENAPI) ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# Configuração para servir arquivos de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)