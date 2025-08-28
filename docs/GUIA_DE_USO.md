

### **Arquivo: `docs/GUIA_DE_USO.md`**

```markdown
# Guia de Uso da Plataforma "A Friend for Life"

Este documento fornece um guia passo a passo sobre como utilizar as principais funcionalidades da plataforma, desde a criação de uma conta até o cadastro de um pet para adoção.

**Pré-requisito:** Antes de começar, certifique-se de que o projeto esteja rodando localmente, seguindo as instruções do arquivo `README.md` principal.

---

### 1. Criando uma Nova Conta

Para cadastrar pets, você primeiro precisa de uma conta de protetor.

1.  **Acesse a Página de Cadastro:** No menu de navegação, clique em "Cadastre-se" ou acesse diretamente a URL [http://127.0.0.1:8000/auth/cadastro/](http://127.0.0.1:8000/auth/cadastro/).

2.  **Preencha o Formulário:** Insira todas as informações solicitadas: nome, sobrenome, e-mail, telefone, localização (estado e cidade) e defina uma senha segura.

3.  **Ative sua Conta (Passo Crucial):**
    *   Após enviar o formulário, o sistema criará sua conta com o status "inativo".
    *   Como estamos em um ambiente de desenvolvimento local, o e-mail de confirmação não será enviado para sua caixa de entrada. Em vez disso, ele será **impresso no terminal** onde você executou o comando `python manage.py runserver`.
    *   **Olhe no seu terminal** e procure por um bloco de texto que começa com `Content-Type: text/html...`. Dentro dele, você encontrará o link de confirmação.
    *   **Copie o link completo** (geralmente começa com `http://127.0.0.1:8000/auth/confirmar_email/...`) e **cole-o na barra de endereço do seu navegador**.
    *   Ao acessar o link, sua conta será ativada e você será redirecionado para a página de login com uma mensagem de sucesso.

### 2. Realizando o Login e Completando o Perfil

1.  **Acesse a Página de Login:** Clique em "Login" ou acesse [http://127.0.0.1:8000/auth/login/](http://127.0.0.1:8000/auth/login/).

2.  **Entre com suas Credenciais:** Use o e-mail e a senha que você acabou de cadastrar.

3.  **Complete seu Perfil (Primeiro Acesso):**
    *   No seu primeiro login, o sistema irá te redirecionar automaticamente para a página "Editar Perfil".
    *   Esta é uma medida de segurança para garantir que todos os protetores tenham informações completas. Geralmente, os dados do cadastro já estarão preenchidos. Apenas confirme se está tudo correto e clique em **"SALVAR"**.
    *   Após salvar, você terá acesso completo a todas as funcionalidades da plataforma.

### 3. Cadastrando um Novo Pet para Adoção

Com seu perfil completo, você já pode ajudar um animal a encontrar um lar!

1.  **Acesse a Página "Novo Pet":** No menu de navegação, clique em "Novo Pet".

2.  **Preencha as Informações do Animal:**
    *   **Fotos:** Faça o upload de uma foto principal (obrigatória) e até 5 fotos secundárias. A interface mostrará uma pré-visualização das imagens.
    *   **Dados Básicos:** Preencha o nome, história, espécie, sexo e tamanho do pet.
    *   **Características:** Selecione as "tags" que melhor descrevem o pet (cuidados, temperamento, etc.).

3.  **Cadastrar:** Após preencher tudo, clique no botão "Cadastrar". Você será redirecionado para a página de listagem de pets com uma mensagem de sucesso.

### 4. Gerenciando Seus Pets

1.  **Acesse seu Perfil:** Clique no ícone de perfil no canto superior direito da navbar e selecione "Meu perfil".

2.  **Visualize Seus Pets:** Na seção "Meus Pets", você verá uma lista de todos os animais que você cadastrou.

3.  **Edite um Pet:**
    *   Clique no botão **"EDITAR"** no card do pet que deseja alterar.
    *   Você será levado a uma página com todos os campos pré-preenchidos.
    *   Faça as alterações necessárias (mudar texto, trocar fotos, etc.) e clique em "Salvar Alterações".

4.  **Remova um Pet:**
    *   Clique no botão **"REMOVER"** no card do pet.
    *   Um modal de confirmação aparecerá para evitar remoções acidentais. Confirme para desativar o anúncio.

5.  **Marque como Adotado:**
    *   Clique no card do pet para ir para a sua página de detalhes (`ver_pet`).
    *   Nesta página, você verá um botão **"Marcar Pet como Adotado"**. Clique nele para atualizar o status do animal.

---

Seguindo este guia, qualquer usuário (incluindo o avaliador) poderá testar todas as funcionalidades principais da sua aplicação de forma clara e objetiva.
```