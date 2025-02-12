usuarios = []

def cadastrar_usuario(nome, email, tipo="cliente"):
    """ 
    Cadastra um novo usuário.
    
    Checklist:
    - [x] Função cadastra um novo usuário.

    Assertivas de Entrada e Saída:
    - Entrada:
        - `nome` (string) - Nome do usuário.
        - `email` (string) - E-mail do usuário.
        - `tipo` (string) - Tipo do usuário (padrão: "cliente").
    - Saída: Nenhuma (o usuário é adicionado à lista `usuarios`).
    """
    usuarios.append({"nome": nome, "email": email, "tipo": tipo})

def listar_usuarios():
    """ 
    Retorna a lista de usuários cadastrados.
    
    Checklist:
    - [x] Função retorna a lista de usuários cadastrados.

    Assertivas de Entrada e Saída:
    - Entrada: Nenhuma.
    - Saída: Lista de usuários cadastrados.
    """
    return usuarios

def buscar_usuario(email):
    """ 
    Busca um usuário pelo e-mail.
    
    Checklist:
    - [x] Função busca um usuário pelo e-mail.

    Assertivas de Entrada e Saída:
    - Entrada: `email` (string) - E-mail do usuário a ser buscado.
    - Saída: Dicionário do usuário encontrado ou `None` se não encontrado.
    """
    return next((u for u in usuarios if u["email"] == email), None)