bancas = []

def listar_bancas():
    """ 
    Retorna a lista de bancas cadastradas.
    
    Checklist:
    - [x] Função retorna a lista de bancas cadastradas.

    Assertivas de Entrada e Saída:
    - Entrada: Nenhuma.
    - Saída: Lista de bancas cadastradas.
    """
    return bancas

def buscar_banca(nome):
    """ 
    Busca uma banca pelo nome.
    
    Checklist:
    - [x] Função busca uma banca pelo nome.

    Assertivas de Entrada e Saída:
    - Entrada: `nome` (string) - Nome da banca a ser buscada.
    - Saída: Dicionário da banca encontrada ou `None` se não encontrada.
    """
    return next((b for b in bancas if nome.lower() in b["nome"].lower()), None)

def cadastrar_banca(nome, localizacao):
    """ 
    Adiciona uma nova banca à lista.
    
    Checklist:
    - [x] Função adiciona uma nova banca à lista.

    Assertivas de Entrada e Saída:
    - Entrada:
        - `nome` (string) - Nome da banca.
        - `localizacao` (string) - Localização da banca.
    - Saída: Nenhuma (a banca é adicionada à lista `bancas`).
    """
    bancas.append({"nome": nome, "localizacao": localizacao})