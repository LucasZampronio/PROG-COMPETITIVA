diaria = int(input())  
aumento = int(input())  
chegada = int(input())  

dias_de_estadia = 32 - chegada 

if chegada <= 15:
    diaria = diaria + (chegada - 1) * aumento
else:
    diaria = diaria + (14 * aumento)

total = dias_de_estadia * diaria

print(total)


