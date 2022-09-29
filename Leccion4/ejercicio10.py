# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caracteres

cadena = input("Digite una cadena de caracteres: ")
lista = []
for i in cadena:
    if i not in lista: # Revisa si el caracter en el iterador no esta en lista
        lista.append(i) # Agrega el caracter a la lista
print(f"Lista de caracteres sin repetir: {lista}")

