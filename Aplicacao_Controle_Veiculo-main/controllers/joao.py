from tkinter import ttk
from tkinter import messagebox
from models.Veiculo import Veiculo
from services.dataBase import session

class Veiculo_view():
    def create_cadastro_veiculo_widgets(self):
        from views.menu_view import cad_veiculo
        
        self.frame_cadastro_veiculo = ttk.Frame(cad_veiculo)
        self.frame_cadastro_veiculo.pack(padx=0, pady=10)

        self.label_placa = ttk.Label(self.frame_cadastro_veiculo, text="Placa:")
        self.label_placa.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.placa_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.placa_entry.grid(row=0, column=1, padx=5, pady=5)

        self.label_chassi = ttk.Label(self.frame_cadastro_veiculo, text="Chassi:")
        self.label_chassi.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.chassi_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.chassi_entry.grid(row=1, column=1, padx=5, pady=5)

        self.label_modelo = ttk.Label(self.frame_cadastro_veiculo, text="Modelo:")
        self.label_modelo.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.modelo_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.modelo_entry.grid(row=2, column=1, padx=5, pady=5)

        self.label_ano_modelo = ttk.Label(self.frame_cadastro_veiculo, text="Ano Modelo:")
        self.label_ano_modelo.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.ano_modelo_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.ano_modelo_entry.grid(row=3, column=1, padx=5, pady=5)

        self.label_hodometro = ttk.Label(self.frame_cadastro_veiculo, text="Hodômetro:")
        self.label_hodometro.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.hodometro_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.hodometro_entry.grid(row=4, column=1, padx=5, pady=5)

        self.label_status_manutencao = ttk.Label(self.frame_cadastro_veiculo, text="Status de Manutenção:")
        self.label_status_manutencao.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.status_manutencao_listbox = ttk.Combobox(self.frame_cadastro_veiculo, values = ["1 - Vencida", "2 - Em dia"])
        self.status_manutencao_listbox.grid(row=5, column=1, padx=5, pady=5)

        self.label_id_categoria = ttk.Label(self.frame_cadastro_veiculo, text="ID da Categoria:")
        self.label_id_categoria.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.id_categoria_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.id_categoria_entry.grid(row=6, column=1, padx=5, pady=5)

        self.label_id_frota = ttk.Label(self.frame_cadastro_veiculo, text="ID da Frota:")
        self.label_id_frota.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.id_frota_entry = ttk.Entry(self.frame_cadastro_veiculo)
        self.id_frota_entry.grid(row=8, column=1, padx=5, pady=5)

        self.btn_cadastrar = ttk.Button(self.frame_cadastro_veiculo, text="Cadastrar veículo", 
                                        command=self.registro_veiculo)
        self.btn_cadastrar.grid(row=10, columnspan=2, pady=10)

    def limpar_campos(self):
        self.placa_entry.delete(0, 'end')
        self.chassi_entry.delete(0, 'end')
        self.modelo_entry.delete(0, 'end')
        self.ano_modelo_entry.delete(0, 'end')
        self.hodometro_entry.delete(0, 'end')
        self.status_manutencao_listbox.set('')
        self.id_categoria_entry.delete(0, 'end')
        self.id_frota_entry.delete(0, 'end')

    def veiculo_info(self):
        placa: str = str(self.placa_entry.get())
        chassi: str = str(self.chassi_entry.get())
        modelo: str = str(self.modelo_entry.get())
        ano_modelo: int = int(self.ano_modelo_entry.get())
        hodometro: int = int(self.hodometro_entry.get())
        status_manutencao: str = str(self.status_manutencao_listbox.get())
        frota_id: int = int(self.id_frota_entry.get())
        categoria_veiculo_id: int = int(self.id_categoria_entry.get())
        
        return placa, chassi, modelo, ano_modelo, hodometro, status_manutencao, categoria_veiculo_id, frota_id
    
    def registro_veiculo(self):
        try:
            veiculo_veiculo = self.veiculo_info()
            placa, chassi, modelo, ano_modelo, hodometro, status_manutencao, categoria_veiculo_id, frota_id = veiculo_veiculo
            
            if status_manutencao == "1 - Vencida":
                status_manutencao = "1"
            else:
                status_manutencao = "2"

            veiculo = Veiculo(placa=placa, chassi=chassi, modelo=modelo, ano_modelo=ano_modelo, hodometro=hodometro, 
                              status_manutencao=status_manutencao, categoria_veiculo_id=categoria_veiculo_id, frota_id=frota_id)
             
            session.add(veiculo)
            session.commit()

            messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o veículo: {e}")