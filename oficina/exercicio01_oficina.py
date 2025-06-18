def buscabinaria(lista, alvo):
    menor = 0
    maior = len(lista) - 1

    while menor <= maior:
        meio = (menor + maior) // 2
        if lista[meio] == alvo:
            resultado = meio
            maior = meio - 1
        elif lista[meio] < alvo:
            menor = meio + 1
        else:
            maior = meio - 1
    return resultado

n = int(input())  
lista = list(map(int, input().split()))  
lista.sort()
alvo = int(input())  
resultado = buscabinaria(lista, alvo)
print(resultado)

