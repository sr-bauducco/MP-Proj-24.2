# MP-Proj-24.2

Este é um sistema de gerenciamento de feiras, onde usuários podem buscar produtos, realizar avaliações e interagir com feirantes. O sistema permite que administradores, feirantes e compradores se cadastrem e acessem diferentes funcionalidades, como o cadastro de produtos, avaliação de feiras, e muito mais.

## Tecnologias Usadas

- **Backend**: Django (Python)
- **Banco de Dados**: SQLite (padrão, mas pode ser configurado para outros bancos)
- **Frontend**: Não especificado (API backend apenas)
- **Autenticação**: Django Rest Framework + JWT (ou autenticação padrão do Django)
- **Migrações**: Django Migrations
- **Serializers**: Django Rest Framework
- **Admin**: Django Admin

## Como Instalar

### Requisitos
- **Python** (recomenda-se a versão 3.8 ou superior)
- **pip** (gerenciador de pacotes do Python)

### Passos para Instalar

1. **Clone o repositório**:
   ```bash
   git clone https://seu-repositorio.git
   cd MP-Proj-24.2
   ```
2. **Crie e ative um ambiente virtual (recomendado):**:
   ```bash
   python -m venv venv
   ```
3. **Instale as dependências do projeto:**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Crie as migrações e aplique-as::**:
   ```bash
   python -m venv venv
   ```
5. **Crie um superusuário (administrador):**:
   ```bash
   python manage.py createsuperuser
   ```
6. **Inicie o servidor de desenvolvimento:**:
   ```bash
   python manage.py runserver
   ```
   Agora, a aplicação estará rodando em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Como Usar

### Endpoints da API

- `POST /auth/register/` - Registro de um novo usuário (comprador ou feirante).
- `POST /auth/login/` - Login de usuário.
- `GET /produtos/` - Lista todos os produtos cadastrados.
- `POST /produtos/` - Cadastro de um novo produto (feirante).
- `GET /feiras/` - Lista todas as feiras.
- `POST /feiras/` - Cadastro de uma nova feira (feirante).
- `POST /avaliacoes/` - Adicionar avaliação a uma feira ou produto.
- `GET /bancas/` - Lista de bancas cadastradas.

### Acesso ao Admin

- **Admin URL**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Faça login com o superusuário criado durante a instalação.

## Contribuindo

Se você deseja contribuir com este projeto, siga estas etapas:

1. **Faça um fork deste repositório.**
2. **Crie uma branch para a nova funcionalidade:**
   ```bash
   git checkout -b feature/nova-funcionalidade
    ```
3. **Faça as alterações e commit:**
    ```bash
    git commit -am 'Adiciona nova funcionalidade'
    ```
4. **Envie a branch para o repositório remoto**
    ```bash
    git push origin feature/nova-funcionalidade
    ```
5. **Abra um pull request para revisar as suas alterações**