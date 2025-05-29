n = int(input())
binario = bin(n)[2:]
binario = str(binario)

if len(binario) % 2 == 0:
    x = len(binario) // 2
    a = binario[0:x]
    
    saida = a + a[::-1]
else:
    saida = binario

saida = int(saida, 2)
print(saida)