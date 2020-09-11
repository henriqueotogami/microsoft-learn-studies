from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

#Além de declarar as funções, treinando as instruções property e setter, o código abaixo obtém todo o objeto da "maquina" no método "escritor.ferramenta".
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

#Como o método "ferramenta" pertence ao escritor, ao excluí-lo, todo o objeto deixa de existir.
del escritor
print (caneta.marca)
maquina.escrever()