class A:
    vc = 123

    def __init__ (self):
        #self.vc = 321
        pass

a1 = A()
a2 = A()

#Note que agora que temos um atributo de instância na classe com o mesmo nome que um atributo da classe. Assim, teremos resultados diferentes. Ao instanciar a classe A como objetos a1 e a2,  valor exibido será 321. No entanto, ao acessar o valor da classe, o valor exibido será 123.
print(a1.vc)
print(a2.vc)
print(A.vc)

#Para que "de fora" seja alterado o valor do atributo da classe, de forma que os objetos, ou melhor, as instâncias sofram alterações, a linha de código "self.vc = 321" do método contrutor deve ser substituída por "pass". Dessa forma, o método construtor fica vazio, neste caso. Acredito que se fosse em uma situação real, era só apagar essa linha, isso porque ela tem o nome do atributo igual ao da classe.
A.vc = 564

#veja:
print(a1.vc)
print(a2.vc)
print(A.vc)