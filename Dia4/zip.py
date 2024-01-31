nombres = ['Ana','Karla','Roberto','Amanda','Vanessa']
edades = [15,27,18,27,27]
conbinados = list(zip(nombres,edades))

for nombre,edad in conbinados:
    print(f"El nombre es {nombre} y su edad es: {edad}")