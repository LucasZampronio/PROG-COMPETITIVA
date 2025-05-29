def buscabinaria(lista, alvo):
    menor = 0
    maior = len(lista) - 1
    contador = 0

    while menor <= maior:
        contador += 1
        meio = (menor + maior) // 2
        if lista[meio] == alvo:
            return contador
        elif lista[meio] < alvo:
            menor = meio + 1
        else:
            maior = meio - 1
    return 'não encontrado'

n = int(input())  
lista = list(map(int, input().split()))  
lista.sort()
alvo = int(input())  
resultado = buscabinaria(lista, alvo)
print(resultado)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.append(11) # adiciona 11 ao final da lista
lista.pop(0) # remove o primeiro elemento da lista
len(lista) # retorna o tamanho da lista
lista.insert(10,11) # insere 11 na posição 10
lista.remove(11) # remove o primeiro elemento 11 da lista
lista.sort() # ordena a lista em ordem crescente
min(lista) # retorna o menor elemento da lista
max(lista) # retorna o maior elemento da lista
sum(lista) # retorna a soma dos elementos da lista
lista.index() # retorna o índice do primeiro elemento encontrado na lista


