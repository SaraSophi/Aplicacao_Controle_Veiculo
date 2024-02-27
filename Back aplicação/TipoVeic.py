class TipoVeic:
    def __init__(self, cod, descricao, categoria):
        self.cod = cod    
        self.descricao = descricao
        self.categoria = categoria

class GerenciadorTipoVeic:
    def __init__(self):
        self.tiposVeic = []

    def inserirTipoVeic(self, cod, descricao, categoria):
        tipoVeic = TipoVeic(cod, descricao, categoria)
        self.tiposVeic.append(tipoVeic)

    def excluirTipoVeic(self, cod):
        for tipoVeic in self.tiposVeic:
            if tipoVeic.cod == cod:
                self.tiposVeic.remove(tipoVeic)
                return True
        return False

    def editarTipoVeic(self, cod, novaDescricao, novaCategoria):
        for tipoVeic in self.tiposVeic:
            if tipoVeic.cod == cod:
                tipoVeic.descricao = novaDescricao
                tipoVeic.categoria = novaCategoria
                return True
        return False

# Exemplo de uso:
gerenciador = GerenciadorTipoVeic()

# Inserindo tipos de veículos
gerenciador.inserirTipoVeic(1, 'Caminhão', 'Pesado')
gerenciador.inserirTipoVeic(2, 'Utilitário', 'Leve')

# Excluindo um tipo de veículo
if gerenciador.excluirTipoVeic(2):
    print("Tipo de veículo excluído com sucesso.")
else:
    print("Tipo de veículo não encontrado.")

# Editando um tipo de veículo
if gerenciador.editarTipoVeic(1, 'Caminhão de Carga', 'Pesado'):
    print("Tipo de veículo editado com sucesso.")
else:
    print("Tipo de veículo não encontrado ou dados inválidos.")
 
print(f"Disponiveis: ", GerenciadorTipoVeic)