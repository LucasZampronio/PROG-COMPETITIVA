import re

n = int(input())
padrao = r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$' 

cpfs = []
for i in range(n):
    cpf = input()
    cpfs.append(cpf)

for cpf in cpfs:
    if re.fullmatch(padrao, cpf):
        print("Válido")
    else:
        print("Inválido")


