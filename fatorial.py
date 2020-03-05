
def fatorial(numero):
    if(numero<0):
        return 0
    if (numero <= 1):
        return 1
    else:
        return numero * fatorial(numero -1)


