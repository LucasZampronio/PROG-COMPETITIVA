d = 5
e = 10
e != 5

g = 15
h = 20
h >= g


g = 15
h = 20
g <= h


idade = 20
if idade >= 18:
    print("Maior de idade")
elif idade == 16:
    print("Pode votar")
else:
    print("Menor de idade")

contador = 0
while contador < 10:
    print("Contador", contador)
    contador += 1

lista = [1, 2, 3, 4, 5]
for numero in lista:
    print("Número:", numero)

# Metodo range cria uma lista 
for numero in range(5):
    print('Número:', numero)


string = "Python"
string.lower()  # Converte para minúsculas
string.upper()  # Converte para maiúsculas
string.startswith("Py")  # Verifica se começa com "Py"
string.endswith("on")  # Verifica se termina com "on"
string.count("o")  # Conta quantas vezes "o" aparece na string
string.isalnum()  # Verifica se a string é alfanumérica
string.isalpha()  # Verifica se a string contém apenas letras
string.split()  # Divide a string em uma lista de substrings
string.strip()  # Remove espaços em branco no início e no final


