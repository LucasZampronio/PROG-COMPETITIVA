def quicksort(array):

    if len(array) <= 1:
        return array
    else:
        pivo = array[0]
        menores = [x for x in array[1:] if x <= pivo]
        maiores = [x for x in array[1:] if x > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
lista = [3,5,2,1,4]
resultado = quicksort(lista)
print(resultado)  



#def quicksort(arry,left,right):
#    if left<right:
#        pi = partition(arry, left, right)
#        quicksort(arry, left, pi - 1)
#        quicksort(arry, pi + 1, right)
#def partition(arry, left, right):
#   pivot = arry[right]
#    i = left - 1
#
#    for j in range(left, right):
#        if arry[j] <= pivot:
#            i += 1
#            arry[i], arry[j] = arry[j], arry[i]
#    arry[i + 1], arry[right] = arry[right], arry[i + 1]
#    return i + 1


#nums = [10, 7, 8, 9, 1, 5]
#quicksort(nums, 0, len(nums) - 1)
#print(nums)