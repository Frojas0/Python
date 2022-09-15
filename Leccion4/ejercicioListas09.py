# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el ususario ingrese una frase, se le devolvera la misma frase pero sin espacios en blanco, y
# ademas un contadir de cuantos caracteres tiene la frase.
# Ejemplo: frase = vivir por siempre en paz
#          frase final = vivirporsiempreenpaz
#          N° de caracteres = 20

frase = input('Digite una frase: ')
fraseFinal = frase.replace(" ", "") # .replace(elemento a reemplazar , elemento)
cont = 0

print(f'''
    Frase inicial: {frase}
    Frase final: {fraseFinal}
    N° de caracteres: {len(fraseFinal)}
    ''')

