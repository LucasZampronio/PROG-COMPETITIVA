# Ler entrada
N = int(input())
M = int(input())
capacidades = list(map(int, input().split()))

baixo = 0
alto = max(capacidades)
resposta = 0

while baixo <= alto:
    meio = (baixo + alto) // 2
    soma = 0

    for c in capacidades:
        if c < meio:
            soma += c
        else:
            soma += meio
        if soma > M:
            break

    if soma <= M:
        resposta = meio
        baixo = meio + 1
    else:
        alto = meio - 1

print(resposta)
