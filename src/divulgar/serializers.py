# divulgar/serializers.py

from rest_framework import serializers
from .models import Pet
from perfil.models import UserProfile

class PetSerializer(serializers.ModelSerializer):
    # Campos extras para enriquecer a API, buscando dados através das relações
    protetor = serializers.ReadOnlyField(source='usuario.userprofile.nome')
    cidade = serializers.ReadOnlyField(source='usuario.userprofile.cidade_nome')
    estado = serializers.ReadOnlyField(source='usuario.userprofile.estado_nome')

    class Meta:
        model = Pet
        fields = [
            'id', 
            'nome_pet', 
            'especie', 
            'sexo', 
            'tamanho', 
            'status', 
            'historia_pet', 
            'protetor', 
            'cidade', 
            'estado',
            'foto_principal'
        ]