from produtos import buscar_produto, ordenar_produtos
from bancas import listar_bancas
from usuarios import cadastrar_usuario, listar_usuarios

produtos = [
    {"nome": "Tomate", "preco": 5.0, "banca": "Banca A", "nota": 4.5},
    {"nome": "Banana", "preco": 3.0, "banca": "Banca B", "nota": 4.7},
    {"nome": "Maçã", "preco": 4.0, "banca": "Banca C", "nota": 4.6}
]

print("📌 Produtos disponíveis:")
for produto in produtos:
    print(f"{produto['nome']} - R$ {produto['preco']} - {produto['banca']} - Nota: {produto['nota']}")

busca = input("\n🔍 Digite o nome do produto que deseja buscar: ")
resultado = buscar_produto(produtos, busca)

if resultado:
    print("\n✅ Produtos encontrados:")
    for p in resultado:
        print(f"{p['nome']} - R$ {p['preco']} - {p['banca']} - Nota: {p['nota']}")
else:
    print("❌ Produto não encontrado!")

print("\n📌 Bancas disponíveis:")
for banca in listar_bancas():
    print(f"{banca['nome']} - Localização: {banca['localizacao']}")


cadastrar_usuario("João", "joao@email.com", "feirante")
print("\n👤 Usuários cadastrados:")
for user in listar_usuarios():
    print(f"{user['nome']} - Tipo: {user['tipo']}")