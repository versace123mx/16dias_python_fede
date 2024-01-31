from random import randint
#nombre = input("Ingresa tu nombre")
numeroMaquina = randint(1,100)

numeroElegido = 0
intento = 0

print(f"numero maquina {numeroMaquina}")

while numeroElegido != numeroMaquina and intento < 8:
    intento +=1
    print(f"Intento numero {intento}")
    numeroElegido = input("Ingresa un numero: ")

    if numeroElegido.isnumeric():
        numeroElegido= int(numeroElegido)
        if numeroElegido < 0 or numeroElegido > 100:
            print(f"El numero {numeroElegido} ingresado tiene que esta entre 1 y 100.")
        elif numeroElegido < numeroMaquina:
            print(f"El numero {numeroElegido} es menor que el numero aleatorio.")
        elif numeroElegido > numeroMaquina:
            print(f"El numero {numeroElegido} es mayor que el numero aleatorio.")
        elif numeroMaquina == numeroElegido:
            print(f"Felicidades el numero aleatorio es: {numeroElegido}.")
            print(f"El numero de intos fue {intento}")

    else:
        print(f"Lo que ingresaste '{numeroElegido}' no es numero.")
        numeroElegido = 0
        intento -=1
    
    if intento >= 8:
        print("Lo sentimos has cumplido con los ocho intentos")
