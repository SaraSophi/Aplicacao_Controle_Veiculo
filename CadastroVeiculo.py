import re

#Tela 1 -  Cadastro Veículo
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


    
class Veiculo:
    def __init__(self, placa, anoVeic,renavam, chassi, tipoVeic, classificacao, modelo, operacao,combustivel):
        #self.frota = frota
        self.placa          = placa
        self.anoVeic        = anoVeic
        self.renavam        = renavam
        self.chassi         = chassi
        self.tipoVeic       = tipoVeic
        self.classificacao  = classificacao
        self.modelo         = modelo
        self.operacao       = operacao
        self.combustivel = combustivel


        '''
            def __init__(self, frota, modelo, combustivel , marca, dtAquisicao, operacao, cor, tracao, qtEixo, classificacao, categoria):
        self.combustivel = combustivel
        self.tipoVeiculo = tipoVeiculo
        self.marca = marca
        self.dtAquisicao = dtAquisicao
        self.operacao = operacao
        self.cor = cor
        self.tracao = tracao
        self.qtEixo = qtEixo
        self.classificacao = classificacao
        '''

    #Validar tamanho caracters/ ordem/ formato
    def validaPlaca(self): 
        # Padrão para validar placa no formato tradicional XXX9999 ou no formato Mercosul ABC1D23
        padraoTradicional = r'^[A-Za-z]{3}\d{4}$'
        padraoMercosul    = r'^[A-Za-z]{3}\d[A-Za-z]\d{2}$'
        if re.match(padraoTradicional, self.placa) or re.match (padraoMercosul, self.placa):
            return True
        else:
            return False
  
    def validaRenavam(self):
        renavam = str(self.renavam).zfill(11)
        if len(renavam) == 9:
            renavam = "00" + renavam
        elif len(renavam) != 11:
            return False
        
        d = [int(x) for x in renavam]
        soma = sum(d[i]*int(peso) for i, peso in enumerate("3298765432"))
        resto = soma % 11
        dv = 11 - resto if resto > 1 else 0
        return dv == d[-1]

    def validaAnoVeic(self):
        #Validação para cadastrar veículos com Ano modelo acima de 2000.
        if self.anoVeic > 2000:
            return True
        else:
            return False
        
    def validaChassi(self):
        #Validação para Chassi - Limitando aos 17 caracters e excluindo I, O e G
        padraoChassi = r'^[A-HJ-NPR-Z0-9]{17}$'
        if re.match(padraoChassi, self.chassi):
            return True
        else:
            return False
    
    #def validaCampos(self):
    #Validação dos campos obrigatorios


# Exemplo de uso

tipoVeic        = TipoVeic(1,'Truck', 'Pesado') 
classificacao   = Classificacao(1,'Caminhão') 
modelos         = ["FH500", "FH400"]
operacoes       = ["1- Linha Fixa", "2- Linha 24hrs"]
tpCombustivel   = ["1- Diesel S10", "2- Diesel S500"]
veiculos        = []
for modelo in modelos:
    for operacao in operacoes:
        for combustivel in tpCombustivel:
            veiculo = Veiculo('abj4h55', 1999, '1345502424', '1G1JC5418R7252367',tipoVeic, 1, modelo, operacao, combustivel)
            veiculos.append(veiculo)

for i, veiculo in enumerate(veiculos, start=1):
    print(f"Veículo {i}:")
    print("Placa:", veiculo.placa)
    print("Ano:", veiculo.anoVeic)
    print("Renavam:", veiculo.renavam)
    print("Chassi:", veiculo.chassi)
    print("Tipo:", veiculo.tipoVeic)
    print("Classificação:", veiculo.classificacao)
    print("Modelo:", veiculo.modelo)
    print("Operação:", veiculo.operacao)
    print("Combustível:",veiculo.combustivel)

    print()

if veiculo.validaPlaca():
    print("Placa válida!")
else:
    print("Placa inválida!")    

if veiculo.validaRenavam():
    print("Renavam válido")
else:
    print("Renavam inválido")

if veiculo.validaAnoVeic():
    print("Ano modelo aceito")
else:
    print("Ano modelo do veículo é inferior a 2000n/ Cadastro não permitido.")

if veiculo.validaChassi():
    print("Chassi válido")
else:
    print("Chassi inválido")

