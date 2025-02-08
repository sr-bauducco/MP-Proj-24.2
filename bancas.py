bancas = []

def listar_bancas():
    """ Retorna a lista de bancas cadastradas """
    return bancas

def buscar_banca(nome):
    """ Busca uma banca pelo nome """
    return next((b for b in bancas if nome.lower() in b["nome"].lower()), None)

def cadastrar_banca(nome, localizacao):
    """ Adiciona uma nova banca à lista """
    bancas.append({"nome": nome, "localizacao": localizacao})