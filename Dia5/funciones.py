from random import shuffle

palitos = ['-','--','---','----']

def mezclar(lista):
    shuffle(lista)
    return  lista

def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    
    return int(intento)


def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)