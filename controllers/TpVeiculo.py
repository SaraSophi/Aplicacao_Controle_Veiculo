class TipoVeic:
    def __init__(self, cod, descricao, categoria):
        self.cod        = cod    
        self.descricao  = descricao
        self.categoria  = categoria

# Lista de valores para adicionar
valoresTipoVeic = [
    (1, "Truck", "Pesado"),
    (2, "Toco", "Pesado"),
    (3, "Carreta", "Pesado"),
    (4, "Bitrem", "Pesado"),
    (5, "Caminhão", "Pesado"),
    (6, "Rodotrem c/ Dolly", "Pesado"),
    (7, "Bi-Truck", "Pesado"),
    (8, "Carreta Bi-truck", "Pesado")
]

# Lista para armazenar as instâncias da classe TipoVeic
tiposVeiculo = []

# Adicionando valores à lista de instâncias
for cod, descricao, categoria in valoresTipoVeic:
    tiposVeiculo.append(TipoVeic(cod, descricao, categoria))

# Apresentar os valores
#for tiposVeiculo in tiposVeiculo:
#    print(f"Código: {tiposVeiculo.cod}, Descrição: {tiposVeiculo.descricao}, Categoria: {tiposVeiculo.categoria}")
if len(tiposVeiculo) == len(valoresTipoVeic):
    print("Valores adicionados, TipoVeic - OK")
else:
    print("Erro ao adicionar valores à lista- TipoVeic")