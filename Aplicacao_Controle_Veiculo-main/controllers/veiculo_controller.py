
import re
from datetime import datetime

#Tela 1 -  Cadastro Veículo
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

# Getters
    def get_placa(self):
        return self.placa

    def get_anoVeic(self):
        return self.anoVeic

    def get_renavam(self):
        return self.renavam

    def get_chassi(self):
        return self.chassi

    def get_tipoVeic(self):
        return self.tipoVeic

    def get_classificacao(self):
        return self.classificacao

    def get_modelo(self):
        return self.modelo

    def get_operacao(self):
        return self.operacao

    def get_combustivel(self):
        return self.combustivel

    def get_dtAquisicao(self):
        return self.dtAquisicao

    def get_cor(self):
        return self.cor

    def get_tracao(self):
        return self.tracao

    def get_qtEixo(self):
        return self.qtEixo

    def get_frota(self):
        return self.frota

    # Setters
    def set_placa(self, placa):
        self.placa = placa

    def set_anoVeic(self, anoVeic):
        self.anoVeic = anoVeic

    def set_renavam(self, renavam):
        self.renavam = renavam

    def set_chassi(self, chassi):
        self.chassi = chassi

    def set_tipoVeic(self, tipoVeic):
        self.tipoVeic = tipoVeic

    def set_classificacao(self, classificacao):
        self.classificacao = classificacao

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_operacao(self, operacao):
        self.operacao = operacao

    def set_combustivel(self, combustivel):
        self.combustivel = combustivel

    def set_dtAquisicao(self, dtAquisicao):
        self.dtAquisicao = dtAquisicao

    def set_cor(self, cor):
        self.cor = cor

    def set_tracao(self, tracao):
        self.tracao = tracao

    def set_qtEixo(self, qtEixo):
        self.qtEixo = qtEixo

    def set_frota(self, frota):
        self.frota = frota


def set_placa(self, placa):
        # Padrão para validar placa no formato tradicional XXX9999 ou no formato Mercosul ABC1D23
        padraoTradicional = r'^[A-Za-z]{3}\d{4}$'
        padraoMercosul = r'^[A-Za-z]{3}\d[A-Za-z]\d{2}$'
        if re.match(padraoTradicional, placa) or re.match(padraoMercosul, placa):
            self.placa = placa
        else:
            raise ValueError("Placa inválida.")

def set_anoVeic(self, anoVeic):
    #Validação para cadastrar veículos com Ano modelo acima de 2000.
    if anoVeic > 2000:
        self.anoVeic = anoVeic
    else:
        raise ValueError("Ano do veículo inválido.")

    def set_renavam(self, renavam):
        renavam = str(renavam).zfill(11)
        if len(renavam) == 9:
            renavam = "00" + renavam
        elif len(renavam) != 11:
            raise ValueError("Renavam inválido.")
        
        d = [int(x) for x in renavam]
        soma = sum(d[i]*int(peso) for i, peso in enumerate("3298765432"))
        resto = soma % 11
        dv = 11 - resto if resto > 1 else 0
        if dv == d[-1]:
            self.renavam = renavam
        else:
            raise ValueError("Renavam inválido.")

    def set_chassi(self, chassi):
        #Validação para Chassi - Limitando aos 17 caracteres e excluindo I, O e G
        padraoChassi = r'^[A-HJ-NPR-Z0-9]{17}$'
        if re.match(padraoChassi, chassi):
            self.chassi = chassi
        else:
            raise ValueError("Chassi inválido.")

    def set_dtAquisicao(self, dtAquisicao):
        separadores = ['-', '/']
        for separador in separadores:
            if separador in dtAquisicao:
                try:
                    datetime.strptime(dtAquisicao, f'%d{separador}%m{separador}%Y')
                    self.dtAquisicao = dtAquisicao
                    return
                except ValueError:
                    pass
        # Se nenhum separador for encontrado na string, tenta inserir "/"
        try:
            dtAquisicao = f"{dtAquisicao[:2]}/{dtAquisicao[2:4]}/{dtAquisicao[4:]}"
            datetime.strptime(dtAquisicao, '%d/%m/%Y')
            self.dtAquisicao = dtAquisicao
            return
        except ValueError:
            raise ValueError("Data de aquisição inválida.")

    def set_qtEixo(self, qtEixo):
        try:
            # Passa eixos para número inteiro
            qtEixo = int(qtEixo)
            # Verifica se a quantidade de eixos está dentro do intervalo aceitável (1 a 10, por exemplo)
            if 1 <= qtEixo <= 10:
                self.qtEixo = qtEixo
            else:
                raise ValueError("Quantidade de eixos inválida.")
        except ValueError:
            # Se não for possível converter para inteiro, retorna False
            raise ValueError("Quantidade de eixos inválida.")


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

tipoVeic        = TipoVeic([{1,'Truck','Pesado'}, {2, 'Bitruck', 'Leve'}])
print(f"Tipo:", tipoVeic.cod,",", tipoVeic.descricao,",", tipoVeic.categoria)
'''