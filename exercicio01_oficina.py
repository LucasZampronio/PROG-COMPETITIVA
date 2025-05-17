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