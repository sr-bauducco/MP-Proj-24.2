usuarios = []

def cadastrar_usuario(nome, email, tipo="cliente"):
    """ Cadastra um novo usuário """
    usuarios.append({"nome": nome, "email": email, "tipo": tipo})

def listar_usuarios():
    """ Retorna a lista de usuários cadastrados """
    return usuarios

def buscar_usuario(email):
    return