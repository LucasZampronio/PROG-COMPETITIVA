def buscamenor(lista):
    menor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i][1] > menor[1]: 
            menor = lista[i]
            menor_indice = i

        elif lista[i][1] == menor[1] and lista[i][0] < menor[0]:
            menor = lista[i]
            menor_indice = i
    return menor_indice

def ordenacaoporselecao(banda):
    nova_lista = []
    for i in range(len(banda)):
        menor = buscamenor(banda)  
        nova_lista.append(banda.pop(menor))
    return nova_lista


n = int(input())
bandas = []

for i in range(n):
    entrada = input().split()
    nome = entrada[0]
    vezes = int(entrada[1])
    bandas.append([nome, vezes])

ordenadas = ordenacaoporselecao(bandas)

for nome, vezes in ordenadas:
    print(f"{nome} {vezes}")


