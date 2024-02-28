
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

    def listarTiposVeic(self):
        return [tipoVeic.descricao for tipoVeic in self.tiposVeic]

gerenciador = GerenciadorTipoVeic()

# Adicionando os tipos de veículos
gerenciador.inserirTipoVeic(1, 'Truck',             'Pesado')
gerenciador.inserirTipoVeic(2, 'Utilitário',        'Leve'  )
gerenciador.inserirTipoVeic(3, 'Toco',              'Pesado')
gerenciador.inserirTipoVeic(4, 'Carreta',           'Pesado')
gerenciador.inserirTipoVeic(5, 'Bitrem',            'Pesado')
gerenciador.inserirTipoVeic(6, 'Caminhão',          'Pesado')
gerenciador.inserirTipoVeic(7, 'Bi-truck',          'Pesado')
gerenciador.inserirTipoVeic(8, 'Rodotrem Dolly',    'Pesado')


# Validando a exclusão 
if gerenciador.excluirTipoVeic(2):
    print("Tipo de veículo excluído com sucesso.")
else:
    print("Tipo de veículo não encontrado.")


# Listando tipos de veículos disponíveis
print("Disponíveis:", gerenciador.listarTiposVeic())