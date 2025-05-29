def soma_recursiva(lista):
    if not lista:
        return 0
    return lista.pop + soma_recursiva(lista)

