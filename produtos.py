def buscar_produto(produtos, nome):
    """ Busca produtos pelo nome """
    return [p for p in produtos if nome.lower() in p["nome"].lower()]

def ordenar_produtos(produtos, criterio="preco"):
    return