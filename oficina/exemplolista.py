
string_dividida = 'Lucas Zampronio Silva'.split()
print(string_dividida)

numeros = int(input().split()) # ERRADO

numeros = map(int, input().split()) # Saída 5,8,12

numeros = list(map(int, input().split())) # Saída: [5, 8, 12]
print(numeros)


