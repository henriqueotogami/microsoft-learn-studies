from datetime import datetime

#Sempre começar o nome da classe com letra maiúscula
#Classe = Objeto
class Pessoa:
    #Neste caso, "ano_atual" é um atributo da classe, porque ele não está dentro de nenhum método. Ou seja, todos os métodos podem acessá-lo.
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    #def = função = método = ação do objeto
    #def __init__ é a contrução, ou base, para os demais métodos
    #self é argumento padrão do método, os demais são opcionais
    def __init__(self, nome, idade, comendo=False, falando=False):

        # atibuto recebe a informação do argumento
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    #Falar é uma ação de uma pessoa
    #Se alguém está falando, então deve ter algum assunto
    #Neste caso, o assunto é o argumento que o método recebe ao ser chamado no arquivo main
    def falar(self, assunto):

        #Verificação se a pessoa está comendo
        #Se a pessoa está comendo, ela não pode falar
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        #Verificação se a pessoa já está falando
        #Se a pessoa está falando, ela continua falando
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        #Se nenhuma das duas verificações acima forem verdadeiras, o método "def falar" faz a pessoa falar sobre o assunto declarado no argumento no arquivo main
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            self.comendo = True

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade