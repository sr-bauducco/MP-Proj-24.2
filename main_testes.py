# test_usuarios.py
from usuarios import cadastrar_usuario, listar_usuarios, buscar_usuario

def test_cadastrar_usuario():
    # Limpa a lista de usuários antes do teste (simulando um estado inicial)
    usuarios = []
    
    # Chama a função cadastrar_usuario
    cadastrar_usuario("João Silva", "joao@example.com")
    
    # Verifica se o usuário foi cadastrado corretamente
    usuario = listar_usuarios()[0]
    assert (usuario["nome"] == "João Silva"
    and usuario["email"] == "joao@example.com"
    and usuario["tipo"] == "cliente")

def test_buscar_usuario():
    # Limpa a lista de usuários antes do teste
    email = "joao@example.com"
    
    # Chama a função cadastrar_usuario
    cadastrar_usuario("João Silva", "joao@example.com")

    assert buscar_usuario(email) != None

