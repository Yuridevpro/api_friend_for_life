from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from perfil.models import UserProfile

class Command(BaseCommand):
    help = 'Cria um usuário de teste para a avaliação da API e da aplicação.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando a criação de dados de teste...'))

        # Define os dados do usuário de teste
        email_teste = 'teste@email.com'
        senha_teste = 'password123'

        # Limpa o usuário de teste antigo para evitar conflitos, se ele existir
        if User.objects.filter(email=email_teste).exists():
            User.objects.get(email=email_teste).delete()
            self.stdout.write(self.style.WARNING(f'Usuário de teste antigo "{email_teste}" removido.'))
        
        # Cria um único usuário de teste
        user = User.objects.create_user(
            username=email_teste, 
            email=email_teste, 
            password=senha_teste, 
            is_active=True # Garante que o usuário já esteja ativo
        )
        
        # Cria o perfil associado ao usuário de teste
        UserProfile.objects.create(
            user=user,
            nome='Usuário',
            sobrenome='Teste',
            telefone='11999999999',
            estado_nome='Ceará',
            estado_id=23, # ID do IBGE para o Ceará
            cidade_nome='Fortaleza',
            email=email_teste
        )
        
        self.stdout.write(self.style.SUCCESS(f'\nUsuário de teste "{email_teste}" criado com sucesso.'))
        self.stdout.write(self.style.SUCCESS('O perfil completo também foi criado.'))
        self.stdout.write(self.style.WARNING(f'Use a senha "{senha_teste}" para testar o login no site, se necessário.'))