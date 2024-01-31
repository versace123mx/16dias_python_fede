texto = input("Ingresa un poema!! : ").lower()
letra1 = input("Ingresa una letra 1: ").lower()
letra2 = input("Ingresa una letra 2: ").lower()
letra3 = input("Ingresa una letra 3: ").lower()
diccionario = {False:'No',True:'Si'}
'''
1) Cuantas veces aparece la letra que ingresaste
2) cuantas palabras hay
3) primera letra del texto y cual es la ultima
4) texto al revez
5) verificar si la palabra python esta en la lista
'''
textoBuscar = 'python' in texto
print(f"El numero de veces que aparece la letra {letra1} es de {texto.count(letra1)} veces")
print(f"El numero de veces que aparece la letra {letra2} es de {texto.count(letra2)} veces")
print(f"El numero de veces que aparece la letra {letra3} es de {texto.count(letra3)} veces")
print(f"El numero de palabras en el texto es {len(texto)} veces")
print(f"La primer letra del texto es {texto[0]}")
print(f"La primer letra del texto es {texto[-1]}")
print(f"El texto al reves es {texto[::-1]}")
print(f"La palabra Python se encuentra en la cadena: {diccionario[textoBuscar]}.")
