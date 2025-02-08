bancas = []

def listar_bancas():
    """ Retorna a lista de bancas cadastradas """
    return bancas

def buscar_banca(nome):
    return

def cadastrar_banca(nome, localizacao):
    """ Adiciona uma nova banca à lista """
    bancas.append({"nome": nome, "localizacao": localizacao})