from random import randint
class Pessoa:

    ano_atual = 2019

    #Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Método da Instância
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    #Método da Classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    #Método Estático
    #Decorador
    #Não depende da classe e nem da instância
    @staticmethod
    def gera_id():
        rand = randint(10000,19999)
        return rand

p1 = Pessoa('Luiz', 32)
print(p1.nome, p1.idade)
p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_nascimento()

#chamada pelo método
print(Pessoa.gera_id())
#Chamada pela instância
print(p1.gera_id())