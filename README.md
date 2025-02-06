q# MP-Proj-24.2

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
   