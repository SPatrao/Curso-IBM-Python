# OPERADORES EN PYTHON
# ======================================
# Objetivo: Proporcionar una guía completa sobre operadores en Python.
# Este archivo cubre operadores aritméticos, de comparación, lógicos,
# de asignación, de pertenencia e identidad, junto con ejemplos y ejercicios prácticos.

# 1. Operadores Aritméticos
# --------------------------------------
# Los operadores aritméticos realizan operaciones matemáticas básicas como suma, resta, multiplicación, etc.

# Pedimos al usuario que ingrese dos números enteros y los convertimos a enteros con `int()`.
a = int(input("Ingresa un número entero (a): "))  # Solicita un número y lo convierte en entero
b = int(input("Ingresa otro número entero (b): "))  # Solicita otro número y lo convierte en entero

# Realizamos las operaciones aritméticas con los dos números introducidos:
suma = a + b  # Suma de a y b
resta = a - b  # Resta de a menos b
multiplicacion = a * b  # Multiplicación de a por b
division = a / b  # División de a entre b (resultado en flotante)
division_entera = a // b  # División entera, parte entera de la división
modulo = a % b  # Residuo de la división de a entre b (módulo)
exponente = a ** b  # a elevado a la potencia de b

# Mostramos los resultados de las operaciones aritméticas.
print(f"{a} + {b} = {suma}")  # Muestra la suma
print(f"{a} - {b} = {resta}")  # Muestra la resta
print(f"{a} * {b} = {multiplicacion}")  # Muestra la multiplicación
print(f"{a} / {b} = {division}")  # Muestra la división
print(f"{a} // {b} = {division_entera}")  # Muestra la división entera
print(f"{a} % {b} = {modulo}")  # Muestra el módulo
print(f"{a} ** {b} = {exponente}")  # Muestra la potencia

# 2. Operadores de Comparación
# --------------------------------------
# Los operadores de comparación permiten comparar dos valores, devolviendo True o False.

# Comparando los números de entrada usando diferentes operadores:
igual = a == b  # Compara si a es igual a b
diferente = a != b  # Compara si a es diferente de b
mayor = a > b  # Compara si a es mayor que b
menor = a < b  # Compara si a es menor que b
mayor_igual = a >= b  # Compara si a es mayor o igual que b
menor_igual = a <= b  # Compara si a es menor o igual que b

# Mostramos los resultados de las comparaciones.
print(f"{a} == {b} → {igual}")  # Muestra si son iguales
print(f"{a} != {b} → {diferente}")  # Muestra si son diferentes
print(f"{a} > {b} → {mayor}")  # Muestra si a es mayor
print(f"{a} < {b} → {menor}")  # Muestra si a es menor
print(f"{a} >= {b} → {mayor_igual}")  # Muestra si es mayor o igual
print(f"{a} <= {b} → {menor_igual}")  # Muestra si es menor o igual

# 3. Operadores Lógicos
# --------------------------------------
# Los operadores lógicos permiten combinar condiciones booleanas (verdadero o falso).

# Definimos dos valores booleanos (True o False):
x = True  # x es verdadero
y = False  # y es falso

# Usamos los operadores lógicos con x e y:
and_logico = x and y  # Devuelve True solo si ambos son True
or_logico = x or y  # Devuelve True si al menos uno es True
not_logico = not x  # Devuelve True si x es False (inverso de x)

# Mostramos los resultados de los operadores lógicos.
print(f"{x} and {y} → {and_logico}")  # Muestra el resultado de and
print(f"{x} or {y} → {or_logico}")  # Muestra el resultado de or
print(f"not {x} → {not_logico}")  # Muestra el resultado de not

# 4. Operadores de Asignación
# --------------------------------------
# Los operadores de asignación modifican el valor de una variable de manera simplificada.

# Pedimos al usuario otro número para usar en operaciones de asignación.
c = int(input("Ingresa un número para operar (c): "))  # Solicita un número y lo convierte en entero

# Usamos operadores de asignación para modificar el valor de c:
c += 2  # Suma 2 a c
print(f"c += 2 → {c}")  # Muestra el valor actualizado de c
c -= 2  # Resta 2 a c
print(f"c -= 2 → {c}")  # Muestra el valor actualizado de c
c *= 2  # Multiplica c por 2
print(f"c *= 2 → {c}")  # Muestra el valor actualizado de c
c /= 2  # Divide c entre 2
print(f"c /= 2 → {c}")  # Muestra el valor actualizado de c
c %= 2  # Asigna a c el residuo de c dividido entre 2
print(f"c %= 2 → {c}")  # Muestra el valor actualizado de c
c **= 2  # Eleva c a la potencia de 2
print(f"c **= 2 → {c}")  # Muestra el valor actualizado de c

# 5. Operadores de Pertenencia
# --------------------------------------
# Los operadores de pertenencia verifican si un elemento está dentro de una secuencia (lista, cadena, etc.).

# Creamos una lista de números
lista = [1, 2, 3, 4, 5]  # Lista de números
# Pedimos al usuario que ingrese un número a buscar en la lista
num = int(input("Ingresa un número para buscar en la lista [1,2,3,4,5]: "))  # Solicita un número

# Verificamos si el número pertenece o no a la lista usando los operadores `in` y `not in`
pertenece = num in lista  # Devuelve True si num está en la lista
no_pertenece = num not in lista  # Devuelve True si num no está en la lista

# Mostramos los resultados de la verificación de pertenencia.
print(f"{num} in lista → {pertenece}")  # Muestra si el número está en la lista
print(f"{num} not in lista → {no_pertenece}")  # Muestra si el número no está en la lista

# 6. Operadores de Identidad
# --------------------------------------
# Los operadores de identidad verifican si dos objetos son el mismo en memoria (referencia al mismo objeto).

# Creamos tres listas
x = [1, 2, 3]  # Lista x
y = [1, 2, 3]  # Lista y
z = x  # z apunta al mismo objeto que x

# Usamos los operadores de identidad para comparar si son el mismo objeto:
es_mismo = x is y  # Devuelve True si x y y son el mismo objeto en memoria
no_mismo = x is not y  # Devuelve True si x y y no son el mismo objeto en memoria
mismo_objeto = x is z  # Devuelve True si x y z son el mismo objeto en memoria

# Mostramos los resultados de la comparación de identidad.
print(f"x is y → {es_mismo}")  # Muestra si x es el mismo objeto que y
print(f"x is not y → {no_mismo}")  # Muestra si x no es el mismo objeto que y
print(f"x is z → {mismo_objeto}")  # Muestra si x es el mismo objeto que z

# 7. Operador Ternario
# --------------------------------------
# El operador ternario es una forma compacta de hacer una estructura condicional simple.

# Usamos el operador ternario para verificar si `a` es par o impar.
resultado = "Par" if a % 2 == 0 else "Impar"  # Si a es divisible por 2, es par; de lo contrario, impar.
print(f"{a} es un número {resultado}")  # Muestra si a es par o impar

# 8. Precedencia de Operadores
# --------------------------------------
# La precedencia de operadores determina el orden en que se ejecutan las operaciones.

resultado_complejo = (a + b) * (a - b) / (a * b)  # Operación que implica varios operadores
print(f"Resultado con precedencia de operadores: {resultado_complejo}")  # Muestra el resultado de la operación compleja

# EJERCICIOS FINALES
# --------------------------------------
print("\n🔹 Ejercicios Finales:")

# Ejercicio 1: Preguntar al usuario por dos números, realizar una operación y mostrar el resultado.
try:
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    suma_ejercicio = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {suma_ejercicio}")
except ValueError:
    print("❌ Error: ¡Por favor, ingresa solo números enteros!")

# Ejercicio 2: Usar el operador ternario para comprobar si un número es mayor que 10.
numero_verificacion = int(input("Ingresa un número para verificar si es mayor que 10: "))
resultado_verificacion = "Mayor que 10" if numero_verificacion > 10 else "No es mayor que 10"
print(f"El número {numero_verificacion} es: {resultado_verificacion}")

# GLOSARIO
# --------------------------------------
print("""
📖 Glosario:
- Operador: Símbolo que realiza una operación en uno o más operandos.
- Aritmético: Relacionado con operaciones matemáticas.
- Lógico: Operaciones basadas en valores de verdad (True o False).
- Comparación: Comparamos dos valores mediante operadores específicos.
""")

