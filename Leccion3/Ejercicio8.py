# EJERCICIO8: Numeros positivos, negativos y neutros
conteoPositivos = 0
conteoNegativos = 0
conteoNeutros = 0

for i in range(0, 10):
    num = int(input("Digite un nÃºmero "+ str(i+1) + ": "))
    if num == 0:
        conteoNeutros += 1
    elif num > 0:
        conteoNegativos += 1
    else:
        conteoPositivos += 1

print("La cantidad de positivos es: ", conteoPositivos)
print("La cantidad de negativos es: ", conteoNegativos)
print("La cantidad de neutros es: ", conteoNeutros)
