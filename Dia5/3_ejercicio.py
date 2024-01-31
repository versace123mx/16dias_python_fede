def numeros(*arg):
    numeroRepeticiones = arg.count(0)
    if numeroRepeticiones >= 2:
        nuevalista = list(arg)
        indice = 0
        for valor in nuevalista:
            if valor == 0:
                if indice >= 1:
                    if valor == nuevalista[indice-1]:
                        return True
            indice += 1
        return False

#print(numeros(0,5,6,1,0,9,3,5,0,0))
#print(numeros(6,0,5,1,0,3,0,1))
#print(numeros(0,5,6,1,0,9,0,3,5,0,1,0))
#print(numeros(5,6,1,9,0,3,5,1,0))
print(numeros(0,5,6,1,9,0,2,3,5,1,0))