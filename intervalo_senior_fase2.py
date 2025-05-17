n_elementos = int(input())
lista = [int(input()) for i in range(n_elementos)]

esquerda,direita = 0,0
unicos = []
tamanho = 0

while direita < len(lista):

    if lista[direita] not in unicos:
        unicos.append(lista[direita])
        direita+= 1

        if direita - esquerda > tamanho:
            tamanho = direita - esquerda
    else:
        unicos.pop(0)
        esquerda+=1
print(tamanho)