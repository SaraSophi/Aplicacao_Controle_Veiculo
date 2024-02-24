import tkinter as tk
from tkinter import ttk, messagebox
import re

class TipoVeic:
    def __init__(self, cod, descricao, categoria):
        self.cod = cod
        self.descricao = descricao
        self.categoria = categoria

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

class Classificacao:
    def __init__(self, cod, descricao):
        self.cod = cod
        self.descricao = descricao

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

class Veiculo:
    def __init__(self, placa, anoVeic, renavam, chassi, tipoVeic, classificacao, modelo, operacao, combustivel):
        self.placa = placa
        self.anoVeic = anoVeic
        self.renavam = renavam
        self.chassi = chassi
        self.tipoVeic = tipoVeic
        self.classificacao = classificacao
        self.modelo = modelo
        self.operacao = operacao
        self.combustivel = combustivel

        self.valido = True  # Flag para verificar se o veículo é válido

    def validaPlaca(self): 
        # Padrão para validar placa no formato tradicional XXX9999 ou no formato Mercosul ABC1D23
        padraoTradicional = r'^[A-Za-z]{3}\d{4}$'
        padraoMercosul = r'^[A-Za-z]{3}\d[A-Za-z]\d{2}$'
        if re.match(padraoTradicional, self.placa) or re.match(padraoMercosul, self.placa):
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
        #Validação para Chassi - Limitando aos 17 caracteres e excluindo I, O e G
        padraoChassi = r'^[A-HJ-NPR-Z0-9]{17}$'
        if re.match(padraoChassi, self.chassi):
            return True
        else:
            return False

class CadastroVeiculo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cadastro de Veículo")

        # Variáveis para armazenar os valores inseridos pelo usuário
        self.placa_var = tk.StringVar(self)
        self.ano_var = tk.StringVar(self)
        self.renavam_var = tk.StringVar(self)
        self.chassi_var = tk.StringVar(self)
        self.tipo_veiculo_var = tk.StringVar(self)
        self.classificacao_var = tk.StringVar(self)
        self.modelo_var = tk.StringVar(self)
        self.operacao_var = tk.StringVar(self)
        self.combustivel_var = tk.StringVar(self)

        # Criando entradas para placa, ano, renavam, chassi
        self.label_placa = ttk.Label(self, text="Placa:")
        self.entry_placa = ttk.Entry(self, textvariable=self.placa_var)
        self.label_placa.grid(row=0, column=0, padx=5, pady=5)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        self.label_ano = ttk.Label(self, text="Ano:")
        self.entry_ano = ttk.Entry(self, textvariable=self.ano_var)
        self.label_ano.grid(row=1, column=0, padx=5, pady=5)
        self.entry_ano.grid(row=1, column=1, padx=5, pady=5)

        self.label_renavam = ttk.Label(self, text="Renavam:")
        self.entry_renavam = ttk.Entry(self, textvariable=self.renavam_var)
        self.label_renavam.grid(row=2, column=0, padx=5, pady=5)
        self.entry_renavam.grid(row=2, column=1, padx=5, pady=5)

        self.label_chassi = ttk.Label(self, text="Chassi:")
        self.entry_chassi = ttk.Entry(self, textvariable=self.chassi_var)
        self.label_chassi.grid(row=3, column=0, padx=5, pady=5)
        self.entry_chassi.grid(row=3, column=1, padx=5, pady=5)

        # Dropdowns para tipo de veículo, classificação, modelo, operação e combustível
        self.label_tipo_veiculo = ttk.Label(self, text="Tipo de Veículo:")
        self.dropdown_tipo_veiculo = ttk.Combobox(self, textvariable=self.tipo_veiculo_var, values=[tipo.descricao for tipo in tiposVeiculo])
        self.label_tipo_veiculo.grid(row=4, column=0, padx=5, pady=5)
        self.dropdown_tipo_veiculo.grid(row=4, column=1, padx=5, pady=5)

        self.label_classificacao = ttk.Label(self, text="Classificação:")
        self.dropdown_classificacao = ttk.Combobox(self, textvariable=self.classificacao_var, values=[classificacao.descricao for classificacao in classificacoes])
        self.label_classificacao.grid(row=5, column=0, padx=5, pady=5)
        self.dropdown_classificacao.grid(row=5, column=1, padx=5, pady=5)

        self.label_modelo = ttk.Label(self, text="Modelo:")
        self.dropdown_modelo= ttk.Combobox(self, textvariable=self.modelo_var, values=["FH500","FH400"])
        self.label_modelo.grid(row=6, column=0, padx=5, pady=5)
        self.dropdown_modelo.grid(row=7, column=1, padx=5, pady=5)


        self.label_operacao = ttk.Label(self, text="Operação:")
        self.dropdown_operacao = ttk.Combobox(self, textvariable=self.operacao_var, values=["Linha Fixa", "Linha 24hrs"])  
        self.label_operacao.grid(row=7, column=0, padx=5, pady=5)
        self.dropdown_operacao.grid(row=7, column=1, padx=5, pady=5)

        self.label_combustivel = ttk.Label(self, text="Combustível:")
        self.dropdown_combustivel = ttk.Combobox(self, textvariable=self.combustivel_var, values=["Diesel S10", "Diesel S500"])  
        self.label_combustivel.grid(row=8, column=0, padx=5, pady=5)
        self.dropdown_combustivel.grid(row=8, column=1, padx=5, pady=5)

        self.button_cadastrar = ttk.Button(self, text="Cadastrar Veículo", command=self.cadastrar_veiculo)
        self.button_cadastrar.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def cadastrar_veiculo(self):
        placa = self.placa_var.get()
        ano = self.ano_var.get()
        renavam = self.renavam_var.get()
        chassi = self.chassi_var.get()
        tipo_veiculo = self.tipo_veiculo_var.get()
        classificacao = self.classificacao_var.get()
        modelo = self.modelo_var.get()
        operacao = self.operacao_var.get()
        combustivel = self.combustivel_var.get()

        # Validando os campos
        veiculo = Veiculo(placa, int(ano), renavam, chassi, tipo_veiculo, classificacao, modelo, operacao, combustivel)
        erros = []
        if not veiculo.validaPlaca():
            erros.append("Placa inválida.")
        if not veiculo.validaRenavam():
            erros.append("Renavam inválido.")
        if not veiculo.validaAnoVeic():
            erros.append("Ano modelo do veículo é inferior a 2000.")
        if not veiculo.validaChassi():
            erros.append("Chassi inválido.")

        if erros:
            messagebox.showerror("Erro", "\n".join(erros))
        else:
            messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso.")

if __name__ == "__main__":
    app = CadastroVeiculo()
    app.mainloop()
