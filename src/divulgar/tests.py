# src/usuarios/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch # Importa a biblioteca de 'mocking'

class LocalidadesAPITests(APITestCase):
    """
    Suite de testes para a API de Localidades.
    """
    def test_list_estados_endpoint(self):
        """
        Testa o endpoint de listagem de estados (GET /api/localidades/estados/).
        """
        url = reverse('api_estado_list')
        response = self.client.get(url)
        
        # Verifica se a requisição foi bem-sucedida (status 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se a resposta contém dados (não está vazia)
        self.assertTrue(len(response.data) > 0)
        # Verifica se a resposta contém um estado conhecido (ex: Ceará)
        nomes_dos_estados = [estado['nome'] for estado in response.data]
        self.assertIn('Ceará', nomes_dos_estados)

    def test_list_cidades_endpoint(self):
        """
        Testa o endpoint de listagem de cidades (GET /api/localidades/estados/<id>/cidades/).
        """
        estado_id_ceara = 23 # ID do Ceará na API do IBGE
        url = reverse('api_cidade_list', kwargs={'estado_id': estado_id_ceara})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
        # Verifica se a resposta contém uma cidade conhecida (ex: Fortaleza)
        nomes_das_cidades = [cidade['nome'] for cidade in response.data]
        self.assertIn('Fortaleza', nomes_das_cidades)

class AvatarAPITests(APITestCase):
    """
    Suite de testes para a API de Avatares.
    """
    def test_get_avatar_endpoint(self):
        """
        Testa o endpoint de geração de avatar (GET /api/avatar/<email>/).
        """
        email_teste = "teste@exemplo.com"
        url = reverse('api_avatar', kwargs={'email': email_teste})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se a resposta contém a chave 'avatar_url'
        self.assertIn('avatar_url', response.data)
        # Verifica se a URL retornada contém a base da API e o e-mail
        self.assertIn('api.dicebear.com', response.data['avatar_url'])
        self.assertIn(email_teste, response.data['avatar_url'])