def quicksort(array):

    if len(array) <= 1:
        return array
    else:
        pivo = array[0]
        menores = [x for x in array[1:] if x <= pivo]
        maiores = [x for x in array[1:] if x > pivo]
    
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
numero = int(input())
valores = list(map(int, input().split()))
ordenada = quicksort(valores)
for i in range(numero):
    if i  == len(ordenada) - 1:
        print(ordenada[i])
    else:
        print(ordenada[i], end=' ')



