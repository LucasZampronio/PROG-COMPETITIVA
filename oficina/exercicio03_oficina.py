def quicksort(array):

    if len(array) <= 1:
        return array
    else:
        pivo = array[0]
        menores = [x for x in array[1:] if x <= pivo]
        maiores = [x for x in array[1:] if x > pivo]
    
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
lista = []
numero = int(input())
valores_energia = int(input().split())
if valores_energia != numero:
    print('')

for valor in valores_energia:
    lista.append(int(valor))

