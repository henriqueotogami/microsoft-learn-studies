class A:
    #Variável de classe ou atributo da classe
    vc = 123


#criando objeto, ou melhor, intanciando a classe
a1 = A()
a2 = A()

#Acessando o atributo da classe criado em cada objeto
print(a1.vc)
print(a2.vc)

#Acessando o atributo da classe na estrutura da classe
print(A.vc)

#Alterando "de fora" o valor do atributo da classe dentro de um objeto, ou seja, na instância
a1.vc = 321
#Da forma acima, o valor de 123 permanece fixo dentro da estrutura da classe, ou seja, A.vc = 123 e a2.vc = 123. Vai mudar somente na estrutura da classe que foi instanciada no objeto "a1".