class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


    
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

#Note que a classe Endereco foi utilizada dentro da classe de Cliente, logo não é necessário realizar a chamada das duas classe, e somente da de Clientes.