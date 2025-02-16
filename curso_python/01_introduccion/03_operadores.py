# OPERADORES EN PYTHON
# --------------------------------------

# 1. Operadores Aritméticos
# Los operadores aritméticos realizan operaciones matemáticas básicas como suma, resta, multiplicación, etc.

# Pedimos al usuario que ingrese dos números enteros y los convertimos a enteros con `int()`.
# `input()` obtiene una cadena de texto, pero necesitamos números enteros para hacer operaciones matemáticas.
a = int(input("Ingresa un número entero (a): "))
b = int(input("Ingresa otro número entero (b): "))

# Realizamos las operaciones aritméticas con los dos números introducidos:
suma = a + b  # Suma de a y b
resta = a - b  # Resta de a menos b
multiplicacion = a * b  # Multiplicación de a por b
division = a / b  # División de a entre b (el resultado es un número flotante)
division_entera = a // b  # División entera, solo la parte entera de la división
modulo = a % b  # El residuo de la división de a entre b (módulo)
exponente = a ** b  # a elevado a la potencia de b (a^b)

# Mostramos los resultados de las operaciones aritméticas.
# La f-string (f"") nos permite insertar variables dentro de un texto de forma sencilla.
print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division}")
print(f"{a} // {b} = {division_entera}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {exponente}")

# 2. Operadores de Comparación
# Los operadores de comparación permiten comparar dos valores, devolviendo True o False.

# Comparamos los dos números de entrada usando diferentes operadores:
igual = a == b  # Compara si a es igual a b
diferente = a != b  # Compara si a es diferente de b
mayor = a > b  # Compara si a es mayor que b
menor = a < b  # Compara si a es menor que b
mayor_igual = a >= b  # Compara si a es mayor o igual que b
menor_igual = a <= b  # Compara si a es menor o igual que b

# Mostramos los resultados de las comparaciones.
print(f"{a} == {b} → {igual}")
print(f"{a} != {b} → {diferente}")
print(f"{a} > {b} → {mayor}")
print(f"{a} < {b} → {menor}")
print(f"{a} >= {b} → {mayor_igual}")
print(f"{a} <= {b} → {menor_igual}")

# 3. Operadores Lógicos
# Los operadores lógicos permiten combinar condiciones booleanas (verdadero o falso).

# Definimos dos valores booleanos (True o False):
x = True  # x es verdadero
y = False  # y es falso

# Usamos los operadores lógicos con x e y:
and_logico = x and y  # Devuelve True solo si ambos son True
or_logico = x or y  # Devuelve True si al menos uno es True
not_logico = not x  # Devuelve True si x es False (inverso de x)

# Mostramos los resultados de los operadores lógicos.
print(f"{x} and {y} → {and_logico}")
print(f"{x} or {y} → {or_logico}")
print(f"not {x} → {not_logico}")

# 4. Operadores de Asignación
# Los operadores de asignación modifican el valor de una variable de manera simplificada.

# Pedimos al usuario otro número para usar en operaciones de asignación.
c = int(input("Ingresa un número para operar (c): "))

# Usamos operadores de asignación para modificar el valor de c:
c += 2  # Suma 2 a c
print(f"c += 2 → {c}")
c -= 2  # Resta 2 a c
print(f"c -= 2 → {c}")
c *= 2  # Multiplica c por 2
print(f"c *= 2 → {c}")
c /= 2  # Divide c entre 2 (el resultado es un flotante)
print(f"c /= 2 → {c}")
c %= 2  # Asigna a c el residuo de c dividido entre 2
print(f"c %= 2 → {c}")
c **= 2  # Eleva c a la potencia de 2
print(f"c **= 2 → {c}")

# 5. Operadores de Pertenencia
# Los operadores de pertenencia verifican si un elemento está dentro de una secuencia (lista, cadena, etc.).

# Creamos una lista de números
lista = [1, 2, 3, 4, 5]
# Pedimos al usuario que ingrese un número a buscar en la lista
num = int(input("Ingresa un número para buscar en la lista [1,2,3,4,5]: "))

# Verificamos si el número pertenece o no a la lista usando los operadores `in` y `not in`
pertenece = num in lista  # Devuelve True si num está en la lista
no_pertenece = num not in lista  # Devuelve True si num no está en la lista

# Mostramos los resultados de la verificación de pertenencia.
print(f"{num} in lista → {pertenece}")
print(f"{num} not in lista → {no_pertenece}")

# 6. Operadores de Identidad
# Los operadores de identidad verifican si dos objetos son el mismo en memoria (referencia al mismo objeto).

# Creamos tres variables con listas.
x = [1, 2, 3]
y = [1, 2, 3]
z = x  # z apunta al mismo objeto que x

# Usamos los operadores de identidad para comparar si son el mismo objeto:
es_mismo = x is y  # Devuelve True si x y y son el mismo objeto en memoria
no_mismo = x is not y  # Devuelve True si x y y no son el mismo objeto en memoria
mismo_objeto = x is z  # Devuelve True si x y z son el mismo objeto en memoria

# Mostramos los resultados de la comparación de identidad.
print(f"x is y → {es_mismo}")
print(f"x is not y → {no_mismo}")
print(f"x is z → {mismo_objeto}")

# 7. Operador Ternario
# El operador ternario es una forma compacta de escribir una estructura condicional simple.

# Usamos el operador ternario para verificar si `a` es par o impar.
resultado = "Par" if a % 2 == 0 else "Impar"  # Si a es divisible por 2, es par; de lo contrario, impar.

# Mostramos el resultado del operador ternario.
print(f"{a} es un número {resultado}")

# 8. Precedencia de Operadores
# La precedencia de operadores determina el orden en que se ejecutan las operaciones.

# Realizamos una operación que involucra varios operadores, y Python respeta la precedencia de operaciones:
resultado_complejo = (a + b) * (a - b) / (a * b)  # Primero se ejecutan las operaciones entre paréntesis.

# Mostramos el resultado de la operación compleja.
print(f"Resultado con precedencia de operadores: {resultado_complejo}")

# ¡Programa finalizado con éxito!
