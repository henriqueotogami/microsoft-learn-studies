class Pessoa:
    #Atributo da classe
    ano_atual = 2019

    #Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Método da instância
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    #Método da classe
    #Método decorador
    #Esse método retorna um objeto "refinado" para a classe "Pessoa". Isso porque o código abaixo está fazendo a conversão, extraindo a idade a partir do ano de nascimento, para que a classe tenha a idade como argumento.
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


#Código abaixo é só para verificação de que a classe está funcionando.
p1 = Pessoa('Luiz', 32)
print(p1.nome, p1.idade)
p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_nascimento()