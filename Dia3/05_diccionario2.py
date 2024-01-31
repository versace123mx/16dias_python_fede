#los diccionarios se pueden cambiar su valor, crear nuevo y eliminar
dic={'c1':['a','b','c'],'c2':['d','e','f']}
dic['c2'][1]='h'
print(dic)
dic['c3']=5
print(dic)
dic.pop('c3')
print(dic)