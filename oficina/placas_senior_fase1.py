placa = input()
formato = True

for caracter in placa:
    letra_maiuscula = ('A' <= caracter <= 'Z')
    digito = ('0' <= caracter <= '9')
    hifen = (caracter == '-')
    
    if not (letra_maiuscula or digito or hifen):
        formato = False
        break

if not formato:
    print('0')  
else:

    if len(placa) == 8:
        letras = placa[0:3]
        hifen = placa[3]
        numeros = placa[4:8]

        if (hifen == '-' and
            letras.isalpha() and  all('A' <= c <= 'Z' for c in letras) and numeros.isdigit()):  
            print('1')
        else:
            print('0')
            
    elif len(placa) == 7:
        if '-' not in placa:
            letrasnovo = placa[0:3]
            numerosnovo = placa[3:7]

            if (letrasnovo.isalpha() and all('A' <= c <= 'Z' for c in letrasnovo) and numerosnovo.isdigit()):   
                print('2')
            else:
                print('0')
        else:
            print('0')
            
    else:
        print('0')

