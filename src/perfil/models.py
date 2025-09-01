from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# NÃO PRECISA importar 'serializers' aqui

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    estado_nome = models.CharField(max_length=100)
    estado_id = models.IntegerField(blank=True, null=True)
    cidade_nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    foto_perfil = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # A CLASSE META E O CAMPO 'avatar_url' NÃO PERTENCEM AO MODELO.
    # Eles foram removidos.

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    # O MÉTODO PARA GERAR A URL DO AVATAR FICA AQUI, NO MODELO.
    def get_avatar(self):
        if self.foto_perfil and hasattr(self.foto_perfil, 'url'):
            return self.foto_perfil.url
        # Gera um avatar único usando o email como 'seed'
        return f"https://api.dicebear.com/8.x/adventurer/svg?seed={self.email}"

   