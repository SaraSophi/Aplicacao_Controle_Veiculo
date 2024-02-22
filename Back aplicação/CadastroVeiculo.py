import re

#Tela 1 -  Cadastro Veículo
class TipoVeic:
    def __init__(self, cod, descricao, categoria):
        self.cod        = cod    
        self.descricao  = descricao
        self.categoria  = categoria

class Classificacao:
    def __init__(self, cod, descricao):
        self.cod        = cod    
        self.descricao  = descricao

    
class Veiculo:
    def __init__(self, placa, anoVeic,renavam, chassi, tipoVeic):
        #self.frota = frota
        #self.modelo = modelo
        self.placa    = placa
        self.anoVeic  = anoVeic
        self.renavam  = renavam
        self.chassi   = chassi
        self.tipoVeic = tipoVeic
        '''
            def __init__(self, frota, modelo, combustivel , marca, dtAquisicao, operacao, cor, tracao, qtEixo, classificacao, categoria):
        self.ano = ano
        self.combustivel = combustivel
        self.tipoVeiculo = tipoVeiculo
        self.renavam = renavam
        self.marca = marca
        self.dtAquisicao = dtAquisicao
        self.operacao = operacao
        self.chassi = chassi
        self.cor = cor
        self.tracao = tracao
        self.qtEixo = qtEixo
        self.dtVinculo = dtVinculo
        self.classificacao = classificacao
        self.categoria = categoria
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

tipoVeic= TipoVeic(1,'Truck', 'Pesado') 
classificacao= Classificacao(1,'Caminhão') 
veiculo = Veiculo('abj4h55', 2020, '1345502424', '1G1JC5418R7252367',tipoVeic )


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

