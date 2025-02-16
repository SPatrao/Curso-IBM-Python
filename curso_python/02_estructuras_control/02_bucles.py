# ESTRUCTURAS DE BUCLE EN PYTHON

# 1. Bucle while: ejecuta un bloque de código mientras una condición sea verdadera.
contador = 0
while contador < 5:  # Mientras el contador sea menor que 5
    print(contador)  # Imprime el valor actual de contador
    contador += 1  # Incrementa el contador en 1 en cada iteración

# 2. While con break: se usa cuando queremos salir del bucle de forma anticipada.
while True:  # Este bucle se ejecutará indefinidamente porque la condición siempre es verdadera
    entrada = input("Ingresa un número (o 'salir' para terminar): ")  # Solicita al usuario que ingrese un número
    if entrada == 'salir':  # Si el usuario ingresa 'salir', terminamos el bucle
        break  # Sale del bucle
    print("Número ingresado:", entrada)  # Imprime el número ingresado

# 3. Bucle for con range: ejecuta un bucle un n1úmero determinado de veces.
for i in range(5):  # El rango va de 0 a 4 (5 no está incluido)
    print(i)  # Imprime los números 0, 1, 2, 3, 4

# 4. For con rango personalizado: podemos especificar el inicio, fin y el paso.
for i in range(2, 10, 2):  # El rango va de 2 a 10, con un paso de 2
    print(i)  # Imprime los números 2, 4, 6, 8

# 5. For con listas: iteramos sobre una lista de elementos.
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:  # Itera sobre cada elemento de la lista "frutas"
    print(fruta)  # Imprime cada fruta: manzana, banana, cereza

# 6. For con enumerate: obtenemos tanto el índice como el valor de cada elemento de la lista.
for indice, fruta in enumerate(frutas):  # Enumerate devuelve el índice y el valor
    print(f"Índice {indice}: {fruta}")  # Imprime el índice y el valor de la fruta

# 7. For con diccionarios: iteramos sobre las claves y valores de un diccionario.
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

for clave, valor in persona.items():  # Itera sobre cada par clave-valor en el diccionario "persona"
    print(f"{clave}: {valor}")  # Imprime la clave y su valor correspondiente

# 8. Bucles anidados: un bucle dentro de otro, se usa cuando necesitamos iterar sobre varias dimensiones.
for i in range(3):  # Bucle exterior
    for j in range(3):  # Bucle interior
        print(f"({i}, {j})")  # Imprime las combinaciones de i y j, como (0, 0), (0, 1), etc.

# 9. Continue y break: "continue" salta la iteración actual y "break" termina el bucle.
for numero in range(10):  # Itera del 0 al 9
    if numero == 3:  # Si el número es 3
        continue  # Salta a la siguiente iteración, es decir, no imprime el 3
    if numero == 8:  # Si el número es 8
        break  # Termina el bucle cuando llega al 8
    print(numero)  # Imprime los números, excepto el 3 (por el continue) y el 8 (por el break)
