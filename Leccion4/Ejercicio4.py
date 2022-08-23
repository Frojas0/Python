# Dada la siguiente tupla
tupla = (13,1,8,3,2,5,8)
# Crear una lista que solo incluya los numeros menores a 5 e imprimir
list = []
for i in tupla:
    if i < 5:
        list.append(i)
print(list)