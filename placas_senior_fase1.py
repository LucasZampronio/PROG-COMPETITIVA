placa = input()

if len(placa) == 8:
    metade = placa.split('-')
    primeira = metade[0]
    segunda = metade[1] 
    if primeira[0].isalpha() and primeira[1].isalpha() and primeira[2].isalpha():
        if segunda[0].isdigit() and segunda[1].isdigit() and segunda[2].isdigit() and segunda[3].isdigit():
            print('1')
elif len(placa) == 7:
    metade = placa.split()
    primeira = metade[0]
    if primeira[0].isalpha() and primeira[1].isalpha() and primeira[2].isalpha() and primeira[3].isdigit() and primeira[4].isdigit() and primeira[5].isdigit() and primeira[6].isdigit():
        print('2')
else: 
    print('0')


""" # USANDO EXPRESSÕES REGULARES
import re

novo = '^[A-Z]{3}[0-9][A-Z][0-9]{2}$'
antigo = '^[A-Z]{3}-[0-9]{4}$'

plate = input()


if re.match(antigo, plate):
    print('1')
elif re.match(novo, plate):
    print('2')
else:
    print('0') """