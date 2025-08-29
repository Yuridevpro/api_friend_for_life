
# divulgar/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Pet
from perfil.models import UserProfile



class PetAPITests(APITestCase):
    """
    Suite de testes para a API de Pets.
    """
    @classmethod
    def setUpTestData(cls):
        """
        Configura os dados iniciais que serão usados em todos os testes desta classe.
        É executado apenas uma vez.
        """
        # 1. Criar um usuário de teste
        cls.user = User.objects.create_user(username='testuser', password='testpassword123')
        
        # 2. Criar um perfil para o usuário de teste
        UserProfile.objects.create(
            user=cls.user,
            nome='Test',
            sobrenome='User',
            telefone='123456789',
            estado_nome='Ceará',
            cidade_nome='Fortaleza',
            email='test@example.com'
        )
        
        # 3. Criar um pet de teste associado a esse usuário
        cls.pet = Pet.objects.create(
            usuario=cls.user,
            nome_pet='Rex',
            especie='Cachorro',
            sexo='Macho',
            tamanho='Médio',
            status='P', # Para Adoção
            is_active=True
        )

    def test_list_pets_endpoint(self):
        """
        Teste para o endpoint de listagem de pets (GET /api/pets/).
        """
        # Monta a URL para o endpoint de listagem
        url = reverse('api_pet_list')
        
        # Faz uma requisição GET para a URL
        response = self.client.get(url, format='json')
        
        # 1. Verifica se a requisição foi bem-sucedida (status code 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. Verifica se a resposta contém 1 resultado (o pet que criamos)
        self.assertEqual(len(response.data), 1)
        
        # 3. Verifica se o nome do pet na resposta está correto
        self.assertEqual(response.data[0]['nome_pet'], 'Rex')

    def test_detail_pet_endpoint(self):
        """
        Teste para o endpoint de detalhes de um pet (GET /api/pets/<id>/).
        """
        # Monta a URL para o endpoint de detalhes, usando o ID do pet que criamos
        url = reverse('api_pet_detail', kwargs={'pk': self.pet.pk})
        
        # Faz uma requisição GET para a URL
        response = self.client.get(url, format='json')
        
        # 1. Verifica se a requisição foi bem-sucedida (status code 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. Verifica se os dados retornados são do pet correto
        self.assertEqual(response.data['nome_pet'], self.pet.nome_pet)
        self.assertEqual(response.data['especie'], 'Cachorro')

    def test_detail_pet_not_found(self):
        """
        Teste para o caso de um pet que não existe.
        """
        # Monta uma URL para um ID de pet que não existe (ex: 999)
        url = reverse('api_pet_detail', kwargs={'pk': 999})
        
        # Faz uma requisição GET
        response = self.client.get(url, format='json')
        
        # Verifica se a API retorna o erro "Not Found" (status code 404)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
