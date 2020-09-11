#Explicação
#public: Em tese, são atributos ou métodos podem ser acessados dentro e fora da classe
#protected: Em tese, são atributos ou métodos que podem ser acessados somente dentro da classe, ou das filhas da classe
#private: Atributo ou método só está disponível dentro da classe.

#Convenção da comunidade
#_ (1 underline) - indica método ou atributo private "mais fraco", que pode ser acessado por fora.
#__ (2 underlines) - indica método ou atributo private "mais forte", que pode ser acessado somente por dentro
class BaseDeDados:
    def __init__(self):
        #Public
        self.__dados = {}

    #Utilizamos essa propriedade para acessar os dados dessa classe corretamente pelo lado de fora, sem utilizar o método ou atributo privado. Além disso, o VSCode avisa como warning quando você está usando um atributo privado.
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()
bd.__dados = 'Outra coisa'

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
#bd.apaga_cliente(2)

bd.lista_clientes()
print(bd.__dados)
print(bd._BaseDeDados__dados)

print(bd.dados)