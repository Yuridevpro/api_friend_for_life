# divulgar/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from perfil.models import UserProfile
from divulgar.models import Pet
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de teste para a API.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando o processo de popular o banco de dados...'))

        # Limpa dados antigos para garantir um estado limpo a cada execução
        User.objects.filter(is_superuser=False).delete()
        Pet.objects.all().delete()
        self.stdout.write('Dados antigos de usuários e pets foram removidos.')

        # --- Cria 2 Usuários Protetores de Teste ---
        for i in range(1, 3):
            username = f'protetor{i}@email.com'
            password = 'password123'
            user = User.objects.create_user(username=username, email=username, password=password, is_active=True) # Cria o usuário como ativo
            
            UserProfile.objects.create(
                user=user,
                nome=f'Protetor {i}',
                sobrenome='Teste',
                telefone=f'1198765432{i}',
                estado_nome='São Paulo',
                cidade_nome='São Paulo',
                email=username
            )
            self.stdout.write(f'Usuário "{username}" e seu perfil foram criados.')

            # --- Cria 3 Pets de Teste para cada Protetor ---
            for j in range(1, 4):
                Pet.objects.create(
                    usuario=user,
                    nome_pet=f'Pet_{i}_{j}',
                    especie=random.choice(['Cachorro', 'Gato']),
                    sexo=random.choice(['Macho', 'Fêmea']),
                    tamanho=random.choice(['Pequeno', 'Médio', 'Grande']),
                    historia_pet=f'Esta é a história do {random.choice(["amável", "brincalhão", "carinhoso"])} Pet_{i}_{j}.',
                    cuidados=['Vacinado', 'Castrado'],
                    vive_bem_em=['Casa'],
                    temperamento=['Calmo', 'Brincalhão'],
                    sociavel_com=['Crianças', 'Cães'],
                    status='P', # Para Adoção
                    is_active=True
                )
        
        self.stdout.write(self.style.SUCCESS(f'\nBanco de dados populado com sucesso! {User.objects.count() - 1} usuários e {Pet.objects.count()} pets foram criados.'))
        self.stdout.write(self.style.WARNING('Você pode usar "protetor1@email.com" ou "protetor2@email.com" com a senha "password123" para testar o login no site.'))