import re 

placa_velha = r'^[A-Z]{3}-[0-9]{4}$'
mercosul = r'^[A-Z]{3}[0-9][A-Z][0-9]$'

placa = input()
if re.match(placa_velha, placa):
    print(1)
elif re.match(mercosul, placa):
    print(2)
else:
    print(0)


#placa = input()

#if 6 <= len(placa) <=8: 
#    if len(placa) == 8 and placa[3] == '-':
#        if (placa[0].isalpha() and
#            placa[1].isalpha() and
#            placa[2].isalpha() and
#            placa[4].isdigit() and
#            placa[5].isdigit() and
#            placa[6].isdigit() and
#            placa[7].isdigit()):
#            print('1')
#        else:
#            print('0')
#
#    elif len(placa) == 7 and '-' not in placa:
#        if (placa[0].isalpha() and
#            placa[1].isalpha() and
#            placa[2].isalpha() and
#            placa[3].isdigit() and
#            placa[4].isdigit() and
#            placa[5].isdigit() and
#            placa[6].isdigit()):
#            print('2')
#        else:
#            print('0')
#    else:
#        print('0')



