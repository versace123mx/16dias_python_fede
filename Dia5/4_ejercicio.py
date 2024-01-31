def es_primo(num):
    acumulador = 0
    for n in range(2, num):
        if num % n == 0:
            pass
        else:
            acumulador +=1
    
    return f"Se encontraron {acumulador} primos"

print(es_primo(50))