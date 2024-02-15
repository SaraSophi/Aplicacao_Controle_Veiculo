import re
from datetime import datetime
from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter import ttk

class Veiculo:
    def __init__(self, frota, modelo, placa, ano, combustivel, tipo_veiculo, renavam, marca, dt_aquisicao, operacao, chassi, cor, tracao, qt_eixo, mot, dt_vinculo, classificacao, categoria):
        self.frota = frota
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.combustivel = combustivel
        self.tipo_veiculo = tipo_veiculo
        self.renavam = renavam
        self.marca = marca
        self.dt_aquisicao = dt_aquisicao
        self.operacao = operacao
        self.chassi = chassi
        self.cor = cor
        self.tracao = tracao
        self.qt_eixo = qt_eixo
        self.mot = mot
        self.dt_vinculo = dt_vinculo
        self.classificacao = classificacao
        self.categoria = categoria

    def validar_renavam(self):
        # Validar RENAVAM com 11 dígitos numéricos
        if not re.match(r'^\d{11}$', self.renavam):
            return False
        return True

    def validar_placa(self):
        # Validar placa no formato AAA-0000
        if not re.match(r'^[a-zA-Z]{3}-\d{4}$', self.placa):
            return False
        return True

    def validar_ano(self):
        # Validar ano do veículo acima de 2000
        if self.ano < 2000:
            return False
        return True

    def validar_data(self, data_str):
        # Validar data no formato DD-MM-YYYY
        try:
            datetime.strptime(data_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False

class VeiculoCadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Veículo")

        # Labels e campos de entrada
        campos = ["Frota:", "Modelo:", "Placa:", "Ano:", "Combustível:", "Tipo de Veículo:", "RENAVAM:", "Marca:", "Data de Aquisição:",
                  "Operação:", "Chassi:", "Cor:", "Tração:", "Quantidade de Eixos:", "Mot:", "Data de Vínculo:", "Classificação:", "Categoria:"]

        self.entries = {}
        for i, campo in enumerate(campos):
            label = Label(root, text=campo)
            label.grid(row=i, column=0, padx=50, pady=5)

            if campo == "Modelo:":
                modelos = ["FH 540", "FH 500", "XF 530 - 411", "FH 460 - 363", "R 460 - 312", "R 450 - 252"]
                entry = ttk.Combobox(root, values=modelos)
            elif campo == "Marca:":
                marcas = ["Volvo", "DAF", "Volkswagen", "Scania", "Mercedes-Benz", "Iveco", "Ford"]
                entry = ttk.Combobox(root, values=marcas)
            elif campo == "Categoria:":
                categorias = ["Leve", "Pesado"]
                entry = ttk.Combobox(root, values=categorias)
            elif campo == "Classificação:":
                classificacoes = ["1-Caminhão", "2-Reboque", "3-SemiReboque", "4-Dolly", "5-Caminhão trator"]
                entry = ttk.Combobox(root, values=classificacoes)
            elif campo == "Tração:":
                tracoes = ["1- Automotor", "2-Reboque/Semirreboque"]
                entry = ttk.Combobox(root, values=tracoes)
            elif campo == "Combustível:":
                combustiveis = ["Diesel S10", "Diesel S500"]
                entry = ttk.Combobox(root, values=combustiveis)
            elif campo == "Cor:":
                cores = ["Branco", "Preto", "Cinza"]
                entry = ttk.Combobox(root, values=cores)
            else:
                entry = Entry(root)

            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[campo] = entry

        # Botão de cadastro
        self.btn_cadastrar = Button(root, text="Cadastrar", command=self.cadastrar_veiculo)
        self.btn_cadastrar.grid(row=len(campos), columnspan=2, pady=10)

    def validar_campos(self):
        # Realizar validação dos campos
        renavam = self.entries["RENAVAM:"].get()
        placa = self.entries["Placa:"].get()
        ano = int(self.entries["Ano:"].get())
        dt_aquisicao = self.entries["Data de Aquisição:"].get()

        if not re.match(r'^\d{11}$', renavam):
            messagebox.showerror("Erro", "RENAVAM inválido")
            return False
        if not re.match(r'^[a-zA-Z]{3}-\d{4}$', placa):
            messagebox.showerror("Erro", "Placa inválida")
            return False
        if ano < 2000:
            messagebox.showerror("Erro", "Ano inválido (deve ser superior a 2000)")
            return False
        try:
            datetime.strptime(dt_aquisicao, '%d-%m-%Y')
        except ValueError:
            messagebox.showerror("Erro", "Data de Aquisição inválida (formato correto: DD-MM-YYYY)")
            return False

        return True

    def cadastrar_veiculo(self):
        if self.validar_campos():
            # Se todos os campos forem válidos, mostra a mensagem de sucesso
            messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso")
            # Aqui você pode adicionar a lógica para salvar os dados em um banco de dados, se necessário

if __name__ == "__main__":
    root = Tk()
    app = VeiculoCadastroApp(root)
    root.mainloop()
