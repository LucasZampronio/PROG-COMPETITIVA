x = int(input('Digite o tamanho da sua lista'))
y = input('1 - Procurar número pares \n2 - Procurar número impares')

for i in range(1,x):
    if y == '1':  
        if i % 2 == 0:
            print(i)
    else:
        if i % 2 != 0:
            print(i)

