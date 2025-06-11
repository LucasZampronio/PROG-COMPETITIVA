N = int(input())
A = int(input())
S = int(input())
maior = -1

for i in range(A):
    soma = 0
    numero = str(i)
    for digito in numero:
        soma += int(digito)
    
    if soma == S and i > maior:
        maior = i  

print(maior)
