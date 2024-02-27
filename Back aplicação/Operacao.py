class Operacao:
    def __init__(self):
        self.operacoes = ["Linha Fixa", "Linha 24hrs"]

    def adicionarOperacao(self, nomeOperacao):
        self.operacoes.append(nomeOperacao)
        print(f"Operação '{nomeOperacao}' adicionada com sucesso.")

    def excluirOperacao(self, nomeOperacao):
        if nomeOperacao in self.operacoes:
            self.operacoes.remove(nomeOperacao)
            print(f"Operação '{nomeOperacao}' excluída com sucesso.")
        else:
            print(f"A operação '{nomeOperacao}' não existe.")

    def editarOperacao(self, nomeOperacaoAntiga, nomeOperacaoNova):
        if nomeOperacaoAntiga in self.operacoes:
            index = self.operacoes.index(nomeOperacaoAntiga)
            self.operacoes[index] = nomeOperacaoNova
            print(f"Operação '{nomeOperacaoAntiga}' alterada para '{nomeOperacaoNova}'.")
        else:
            print(f"A operação '{nomeOperacaoAntiga}' não existe.")

operacao = Operacao()

#Testes para uso 
'''
# Adicionando operações
operacao.adicionarOperacao("Linha Fixa")
operacao.adicionarOperacao("Linha 24hrs")
operacao.adicionarOperacao("Linha Alimentos")

# Excluindo operação
operacao.excluirOperacao("Linha Alimentos")

# Tentando excluir uma operação inexistente
operacao.excluirOperacao("Linhas")

# Editando operação
operacao.editarOperacao("Linha Fixa", "Linha Alimentos")
'''
# Visualizando as operações
print("Operações disponíveis:", operacao.operacoes)

