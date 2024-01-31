def devolver_distintos(a,b,c):
    operacion = a+b+c
    lista = [a,b,c]
    if operacion > 15:
        return max(lista)
    elif operacion < 10:
        return min(lista)
    elif operacion in range(10,16):
        lista.sort()
        return lista[1] 

print(devolver_distintos(12,2,1))