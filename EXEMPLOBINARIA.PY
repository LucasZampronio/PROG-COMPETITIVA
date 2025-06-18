def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        print(meio)
        if lista[meio] == item:
            return meio
        elif lista[meio] < item:
            baixo = meio + 1
        else:
            alto = meio - 1


lista = range(100000000)

numero_procurado = 9000000
indice = busca_binaria(lista, numero_procurado)
