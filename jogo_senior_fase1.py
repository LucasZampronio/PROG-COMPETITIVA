
linhas = int(input())
colunas = int(input())
matriz = []
for i in range(linhas):
    lista = []  
    for j in range(colunas):
        lista.append(j)  
    matriz.append(lista)  


for linha in matriz:
    print(linha)
