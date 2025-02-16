# VARIABLES

# Declaración de variables
mensaje = "Hola, mundo"
edad = 25
pi = 3.14159
es_mayor = True

# Asignación de una variable a otra
mensaje2 = mensaje
print(mensaje2)

# Declaración múltiple
a, b, c = 'string', 15, True
print(a, b, c)

# Declaración de constante
NUMEROPI = 3.14159
print(NUMEROPI)

# CASTING

x = int(2.8)  # x será 2
y = float("4.5")  # y será 4.5
z = str(100)  # z será '100'
print(x, y, z)

# COMENTARIOS

# Esto es un comentario de una línea
"""
Esto es un comentario de varias líneas
"""

# OPERADORES

suma = 10 + 5
resta = 10 - 3
multiplicacion = 4 * 3
division = 10 / 2
modulo = 10 % 3
print(suma, resta, multiplicacion, division, modulo)

# Operadores lógicos
print(10 > 5)
print(10 == 10)
print(10 != 5)

# ENTRADA Y SALIDA DE DATOS

tu_nombre = input("Introduce tu nombre: ")
print("Hola, " + tu_nombre + "!")

# STRINGS

texto = "Hola Mundo"
print(texto.lower())
print(texto.upper())
print(texto.replace("Mundo", "Python"))

# TIPOS DE DATOS MUTABLES E INMUTABLES

lista = [1, 2, 3]
lista.append(4)
print(lista)

tupla = (1, 2, 3)
# tupla[0] = 10  # Esto dará error

# DIRECCIONES DE MEMORIA

a = 65
print("Dirección de memoria de a:", id(a))

b = a
print("Dirección de memoria de b:", id(b))

a += 2
print("Nueva dirección de memoria de a:", id(a))
