
candidatos, aprovados = map(int, input().split())
notas = list(map(int, input().split()))
notas.sort()
nota_corte = notas[-aprovados]

print(nota_corte)
