# ESTRUCTURAS DE BUCLE EN PYTHON
# ======================================
# Objetivo: Proporcionar una guía completa sobre las estructuras de bucle en Python.
# Este archivo cubre los bucles while y for, junto con sus variaciones y ejemplos prácticos.

# 1. Bucle while: ejecuta un bloque de código mientras una condición sea verdadera.
# Inicializamos un contador
contador = 0
print("🔹 Bucle while:")
while contador < 5:  # Evaluamos si el contador es menor que 5
    print(contador)  # Imprimimos el valor actual del contador
    contador += 1  # Incrementamos el contador en 1

# 2. While con break: se usa para salir del bucle de forma anticipada.
print("\n🔹 Bucle while con break:")
while True:  # Este bucle se ejecutará indefinidamente
    entrada = input("Ingresa un número (o 'salir' para terminar): ")  # Solicitamos un número al usuario
    if entrada == 'salir':  # Si el usuario ingresa 'salir'
        break  # Terminamos el bucle
    print("Número ingresado:", entrada)  # Imprimimos el número ingresado

# 3. Bucle for con range: ejecuta un bucle un número determinado de veces.
print("\n🔹 Bucle for con range:")
for i in range(5):  # El rango va de 0 a 4 (5 no está incluido)
    print(i)  # Imprimimos los números del 0 al 4

# 4. For con rango personalizado: especificamos el inicio, fin y el paso.
print("\n🔹 For con rango personalizado:")
for i in range(2, 10, 2):  # El rango va de 2 a 10, con un paso de 2
    print(i)  # Imprimimos los números 2, 4, 6, 8

# 5. For con listas: iteramos sobre una lista de elementos.
print("\n🔹 For con listas:")
frutas = ["manzana", "banana", "cereza"]  # Lista de frutas
for fruta in frutas:  # Iteramos sobre cada elemento de la lista "frutas"
    print(fruta)  # Imprimimos cada fruta: manzana, banana, cereza

# 6. For con enumerate: obtenemos tanto el índice como el valor de cada elemento de la lista.
print("\n🔹 For con enumerate:")
for indice, fruta in enumerate(frutas):  # Enumerate devuelve el índice y el valor
    print(f"Índice {indice}: {fruta}")  # Imprimimos el índice y el valor de la fruta

# 7. For con diccionarios: iteramos sobre las claves y valores de un diccionario.
print("\n🔹 For con diccionarios:")
persona = {  # Diccionario con información de una persona
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
for clave, valor in persona.items():  # Iteramos sobre cada par clave-valor en el diccionario "persona"
    print(f"{clave}: {valor}")  # Imprimimos la clave y su valor correspondiente

# 8. Bucles anidados: un bucle dentro de otro, se usa para iterar sobre múltiples dimensiones.
print("\n🔹 Bucles anidados:")
for i in range(3):  # Bucle exterior
    for j in range(3):  # Bucle interior
        print(f"({i}, {j})")  # Imprime las combinaciones de i y j, como (0, 0), (0, 1), etc.

# 9. Continue y break: "continue" salta la iteración actual y "break" termina el bucle.
print("\n🔹 Continue y break:")
for numero in range(10):  # Iteramos del 0 al 9
    if numero == 3:  # Si el número es 3
        continue  # Salta esta iteración, es decir, no imprime el 3
    if numero == 8:  # Si el número es 8
        break  # Termina el bucle cuando llega al 8
    print(numero)  # Imprime los números, excepto el 3 (por el continue) y el 8 (por el break)

# EJERCICIOS FINALES
# ======================================
print("\n🔹 Ejercicios Finales:")

# Ejercicio 1: Usar un bucle while para contar del 0 al 10
print("\nEjercicio 1: Contar del 0 al 10")
contador = 0
while contador <= 10:  # Sustituye <= con < si deseas contar sólo del 0 al 9.
    print(f"Contador: {contador}")
    contador += 1  # Incrementa el contador

# Ejercicio 2: Usar un bucle for para imprimir los números del 1 al 10 y sus cuadrados.
print("\nEjercicio 2: Números y sus cuadrados del 1 al 10")
for i in range(1, 11):  # Contamos del 1 al 10
    print(f"Número: {i}, Cuadrado: {i**2}")  # Imprimimos el número y su cuadrado

# GLOSARIO
# ======================================
print("""
📖 Glosario:
- Bucle: Estructura que permite repetir un bloque de código mientras una condición sea verdadera.
- While: Bucle que se ejecuta mientras la condición especificada sea verdadera.
- For: Bucle que se utiliza para iterar sobre elementos de una secuencia (lista, rango, diccionario, etc.).
- Continue: Instrucción que salta la iteración actual y continúa con la siguiente.
- Break: Instrucción que termina el bucle inmediatamente.
- Enumerate: Función que permite iterar sobre un objeto iterable y obtener tanto el índice como el valor de los elementos.
""")

