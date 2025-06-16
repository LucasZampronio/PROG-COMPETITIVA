resultados = [] 
for lista in range(6):
    resultado = input()
    resultados.append(resultado)

vitorias = 0
for vitoria in resultados:
    if vitoria.upper() == 'V':
        vitorias += 1
        
if vitorias >= 5:
    print(1)
elif vitorias >= 3:
    print(2)
elif vitorias >= 1:
    print(3)
else:
    print(-1)


