# src/divulgar/serializers.py (VERSÃO CORRIGIDA)

from rest_framework import serializers
from .models import Pet
from perfil.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializer para expor os dados públicos do perfil do protetor. """
    class Meta:
        model = UserProfile
        # Lista dos campos do perfil que serão expostos
        fields = ['nome', 'sobrenome', 'telefone', 'email']

class PetSerializer(serializers.ModelSerializer):
    # Agora, o campo 'usuario' usará o UserProfileSerializer
    # para aninhar um objeto completo com os dados do protetor.
    usuario = UserProfileSerializer(source='usuario.userprofile', read_only=True)
    
    # Estes campos de cidade e estado são redundantes, mas podemos manter se quiser
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
            'usuario',  # <-- Este campo agora conterá o objeto aninhado
            'cidade', 
            'estado',
            'foto_principal'
        ]

