class Classificacao:
    def __init__(self, cod, descricao):
        self.cod        = cod    
        self.descricao  = descricao

# Lista de valores para adicionar
valoresClassificacao = [
    (1, "Caminhão"),
    (2, "Reboque"),
    (3, "SemiReboque"),
    (4, "Dolly"),
    (5, "Caminhão trator")
]
# Lista para armazenar as instâncias da classe Classificacao
classificacoes = []

# Adicionando valores à lista de instâncias
for cod, descricao in valoresClassificacao:
    classificacoes.append(Classificacao(cod, descricao))

# Apresentar na tela
#for classificacao in classificacoes:
#   print(f"Código: {classificacao.cod}, Descrição: {classificacao.descricao}")

# Validando se os valores foram adicionados corretamente
if len(classificacoes) == len(valoresClassificacao):
    print("Valores adicionados, Classificações - OK")
else:
    print("Erro ao adicionar valores à lista- Classificações")
