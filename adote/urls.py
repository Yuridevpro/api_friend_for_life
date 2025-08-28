# adote/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from divulgar.views import PetListAPIView, PetDetailAPIView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('divulgar/', include('divulgar.urls')),
    path('adotar/', include('adotar.urls')),
    path('perfil/', include('perfil.urls')),
    path('sobre_nos/', include('sobre_nos.urls')),
    path('pagina_inicio/', include('pagina_inicio.urls')),
    path('', RedirectView.as_view(url='/pagina_inicio/', permanent=False)),  # Redireciona para a página inicial
    path('api/pets/', PetListAPIView.as_view(), name='api_pet_list'),
    path('api/pets/<int:pk>/', PetDetailAPIView.as_view(), name='api_pet_detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Rotas para a interface visual da documentação
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
