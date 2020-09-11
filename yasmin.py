def remove_repetidos(lista2):
    y = int(input("Tamanho de sua lista: "))
    lista = []
    while len(lista) < y:
        x = int(input("Digite: "))
        lista.append(x)
        lista1 = list(set(lista))
        lista2 = sorted(lista1)
    return lista2


remove_repetidos(2)