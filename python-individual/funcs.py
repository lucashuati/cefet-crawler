def maior(a, b):
    return a if a > b else b


def soma(lista, x=0):
    total = 0
    for l in lista:
        total += l
    return total + x


def media(lista):
    tam_lista = len(lista)
    if tam_lista == 0:
        return 0

    total = soma(lista)
    return total / tam_lista


def valores_iguais(lista1, lista2):
    comum = []
    for l1 in lista1:
        for l2 in lista2:
            if l1 == l2:
                comum.append(l1)
    return comum


def indice_prim_valor_igual(lista1, lista2):
    indice = 0
    for l1 in lista1:
        for l2 in lista2:
            if l1 == l2:
                return indice
        indice += 1
    return None
