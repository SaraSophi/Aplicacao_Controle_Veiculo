
import re
from datetime import datetime
from Operacao import Operacao



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
    def __init__(self, placa, anoVeic,renavam, chassi, tipoVeic, classificacao, modelo, operacao, combustivel, dtAquisicao, cor, tracao, qtEixo, frota):
        self.placa          = placa
        self.anoVeic        = anoVeic
        self.renavam        = renavam
        self.chassi         = chassi
        self.tipoVeic       = tipoVeic
        self.classificacao  = classificacao
        self.modelo         = modelo
        self.operacao       = operacao
        self.combustivel    = combustivel
        self.dtAquisicao    = dtAquisicao
        self.cor            = cor
        self.tracao         = tracao
        self.qtEixo         = qtEixo
        self.frota          = frota

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

    def validaData(self):
        separadores = ['-', '/']
        for separador in separadores:
            if separador in self.dtAquisicao:
                try:
                    datetime.strptime(self.dtAquisicao, f'%d{separador}%m{separador}%Y')
                    return True
                except ValueError:
                    pass
        # Se nenhum separador for encontrado na string, tenta inserir "/"
        try:
            self.dtAquisicao = f"{self.dtAquisicao[:2]}/{self.dtAquisicao[2:4]}/{self.dtAquisicao[4:]}"
            datetime.strptime(self.dtAquisicao, '%d/%m/%Y')
            #teste para ve se mudou mesmo - APAGAR
            print(f"{self.dtAquisicao}")
            return True
        except ValueError:
            return False


        #def validaCampos(self):
        #Validação dos campos obrigatorios

    def validaQtdEixo(self):
        try:
            # Passa eixos para número inteiro
            self.qtEixo = int(self.qtEixo)
            # Verifica se a quantidade de eixos está dentro do intervalo aceitável (1 a 10, por exemplo)
            if self.qtEixo == '':
                print("A quantidade de eixo deve ser informada.")
                return ValueError
            else:   

                if 1 <= self.qtEixo <= 10:
                    return True
                else:
                    return False
        except ValueError:
                # Se não for possível converter para inteiro, retorna False
                return False

   # def validaFrota(self):
    #    if self.tracao = 1  se for automotor incrementar

# Valores
''' 
tipoVeic        = TipoVeic(1,'Truck','Pesado')
classificacao   = Classificacao(1,'Caminhão') 
clOperacao      = Operacao()
#clOperacao.adicionarOperacao("KKJnhkjkjhglkjh")
operacoes       = clOperacao.operacoes
modelos         = ["FH500 - Volvo", "FH400 - Volvo"]
tpCombustivel   = ["1- Diesel S10", "2- Diesel S500"]
cores           = ["Branco", "Preto", "Cinza"]
tpTracao        = ["Automotor", "Reboque", "SemiReboque"]

veiculos        = []
for modelo in modelos:
    for operacao in operacoes:
        for combustivel in tpCombustivel:
            for cor in cores:
                for tracao in tpTracao:
                    veiculo = Veiculo('abj4h55', 2021, '1345502424', '1G1JC5418R7252367',tipoVeic, 1, modelo, operacao, combustivel, '20122024', cor, tracao, 1)
                    veiculos.append(veiculo)

for i, veiculo in enumerate(veiculos, start=1):
    print(f"Veículo {i}:")
    print("Placa:", veiculo.placa)
    print("Ano:", veiculo.anoVeic)
    print("Renavam:", veiculo.renavam)
    print("Chassi:", veiculo.chassi)
    print("Tipo:", veiculo.tipoVeic.cod,",", veiculo.tipoVeic.descricao,",", veiculo.tipoVeic.categoria)
    print("Classificação:", veiculo.classificacao)
    print("Modelo:", veiculo.modelo)
    print("Operação:", veiculo.operacao)
    print("Combustível:",veiculo.combustivel)
    print("Data de Aquisição:",veiculo.dtAquisicao)
    print("Cor Predominante:",veiculo.cor)
    print("Tração:",veiculo.tracao)
    print("Eixos:",veiculo.qtEixo)
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

if veiculo.validaData():
    print("Data válido")
else:
   print("Data inválido")

if veiculo.validaQtdEixo():
    print("Quantidade de eixos válida.")
else:
    print("Quantidade de eixos inválida.")
'''
tipoVeic        = TipoVeic([{1,'Truck','Pesado'}, {2, 'Bitruck', 'Leve'}])
print(f"Tipo:", tipoVeic.cod,",", tipoVeic.descricao,",", tipoVeic.categoria)
