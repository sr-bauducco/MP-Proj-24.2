# test_usuarios.py
from usuarios import cadastrar_usuario, listar_usuarios

def test_cadastrar_usuario():
    # Limpa a lista de usuários antes do teste (simulando um estado inicial)
    usuarios = []
    
    # Chama a função cadastrar_usuario
    cadastrar_usuario("João Silva", "joao@example.com")
    
    # Verifica se o usuário foi cadastrado corretamente
    usuarios = listar_usuarios()[0]
    assert (usuarios["nome"] == "João Silva"
    and usuarios["email"] == "joao@example.com"
    and usuarios["tipo"] == "cliente")