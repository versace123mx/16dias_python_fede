def eliminda_duplicados(cadena):
    eliminaduplicados = list(set(cadena))
    eliminaduplicados.sort()
    return eliminaduplicados

print(eliminda_duplicados('entretenido'))