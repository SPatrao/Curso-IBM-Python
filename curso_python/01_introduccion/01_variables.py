# VARIABLES EN PYTHON
# ------------------------------
# Guía completa de declaración y uso

# Introducción a los tipos básicos de variables
print("\n📌 TIPOS BÁSICOS DE VARIABLES")

# **Enteros (int)**: Son números enteros, positivos o negativos.
print("\n🔹 Variables de tipo entero (int):")
edad = 25  # Una variable llamada 'edad' que guarda el valor 25 (entero)
print("Edad (int): " + str(edad))  # Convertimos la variable a string para poder mostrarla
contador = -10  # Un número entero negativo
print("Contador (int): " + str(contador))  # Mostramos la variable 'contador'

# **Flotantes (float)**: Son números con decimales.
print("\n🔹 Variables de tipo flotante (float):")
altura = 1.75  # Una variable de tipo flotante que guarda el valor 1.75
temperatura = -5.6  # Otro número flotante negativo
print("Altura (float): " + str(altura))  # Mostramos la variable 'altura'
print("Temperatura (float): " + str(temperatura))  # Mostramos la variable 'temperatura'

# **Cadenas de texto (str)**: Son secuencias de caracteres.
print("\n🔹 Variables de tipo cadena de texto (str):")
nombre = "Juan Pérez"  # Una cadena de texto con un nombre
mensaje = 'Hola, mundo'  # Otra cadena de texto con un saludo
multilinea = """Este es un texto
que ocupa varias líneas"""  # Cadena de texto que ocupa varias líneas
print("Nombre (str): " + nombre)  # Mostramos el nombre
print("Mensaje (str): " + mensaje)  # Mostramos el mensaje
print("Texto Multilínea (str): " + multilinea)  # Mostramos el texto multilínea

# **Booleanos (bool)**: Son valores que pueden ser True (verdadero) o False (falso).
print("\n🔹 Variables de tipo booleano (bool):")
es_estudiante = True  # La variable 'es_estudiante' es True (verdadero)
tiene_trabajo = False  # La variable 'tiene_trabajo' es False (falso)
print("Es estudiante (bool): " + str(es_estudiante))  # Mostramos si es estudiante
print("Tiene trabajo (bool): " + str(tiene_trabajo))  # Mostramos si tiene trabajo

# **Declaración múltiple**: Se pueden declarar varias variables en una sola línea.
print("\n🔹 Declaración de múltiples variables en una sola línea:")
x, y, z = 1, 2, 3  # Asignamos 1 a x, 2 a y y 3 a z en una sola línea
print(f"x: {x}, y: {y}, z: {z}")  # Mostramos las variables x, y, z

# CONVERSIÓN DE TIPOS (CASTING)
# ---------------------------------------
print("\n📌 CONVERSIÓN DE TIPOS (CASTING)")

# **str a int**: Convertir una cadena de texto en un número entero
print("\n🔹 Convertir cadena a entero (str → int):")
edad_str = "30"  # La cadena de texto "30"
edad_int = int(edad_str)  # Convertimos la cadena "30" a un número entero
print("Edad como entero: " + str(edad_int))  # Mostramos la edad como entero

# **int a float**: Convertir un número entero en un flotante
print("\n🔹 Convertir entero a flotante (int → float):")
edad_float = float(edad)  # Convertimos la variable 'edad' (que es un entero) a un flotante
print("Edad como flotante: " + str(edad_float))  # Mostramos la edad como flotante

# **float a int**: Convertir un número flotante en un entero
print("\n🔹 Convertir flotante a entero (float → int):")
altura_int = int(altura)  # Convertimos el número flotante 'altura' a entero (se pierde la parte decimal)
print("Altura como entero: " + str(altura_int))  # Mostramos la altura como entero

# FUNCIONES ÚTILES
# ---------------------------------------
print("\n📌 FUNCIONES ÚTILES")
# **Verificar el tipo de una variable con type()**: La función 'type()' muestra el tipo de dato de una variable
print("\n🔹 Verificar el tipo de una variable con type():")
print("Tipo de edad: " + str(type(edad)))  # Muestra el tipo de la variable 'edad', que es int
print("Tipo de nombre: " + str(type(nombre)))  # Muestra el tipo de la variable 'nombre', que es str

# BUENAS PRÁCTICAS EN PYTHON
# ---------------------------------------
print("\n📌 BUENAS PRÁCTICAS EN PYTHON")
print("- Usar nombres en snake_case para variables.")  # Es recomendable usar letras minúsculas y separar las palabras con guiones bajos (e.g., 'edad_usuario')
print("- Usar nombres descriptivos en lugar de letras sueltas.")  # Es mejor usar nombres como 'edad' en lugar de 'e'
print("- Evitar nombres excesivamente cortos o sin significado.")  # Evitar nombres poco claros

# OPERADORES EN PYTHON
# ---------------------------------------
print("\n📌 OPERADORES EN PYTHON")

# **Operadores Aritméticos**: Son los operadores básicos para realizar cálculos matemáticos.
a = int(input("\nIngresa un número entero (a): "))
b = int(input("Ingresa otro número entero (b): "))

print("\n🔹 Operaciones aritméticas con los números ingresados:")
# Suma, Resta, Multiplicación, División, División entera, Módulo, Potencia
print(f"Suma: {a} + {b} = {a + b}")  # Muestra la suma de a y b
print(f"Resta: {a} - {b} = {a - b}")  # Muestra la resta de a y b
print(f"Multiplicación: {a} * {b} = {a * b}")  # Muestra la multiplicación de a y b
print(f"División: {a} / {b} = {a / b}")  # Muestra la división de a entre b
print(f"División entera: {a} // {b} = {a // b}")  # Muestra la división entera (sin decimales)
print(f"Módulo: {a} % {b} = {a % b}")  # Muestra el residuo de la división de a entre b
print(f"Potencia: {a} ** {b} = {a ** b}")  # Muestra a elevado a b

# **Operadores de Comparación**: Compara dos valores y devuelve un valor booleano (True o False).
print("\n🔹 Comparaciones entre los números ingresados:")
print(f"{a} == {b} : {a == b}")  # Compara si a es igual a b
print(f"{a} != {b} : {a != b}")  # Compara si a es diferente de b
print(f"{a} > {b} : {a > b}")  # Compara si a es mayor que b
print(f"{a} < {b} : {a < b}")  # Compara si a es menor que b
print(f"{a} >= {b} : {a >= b}")  # Compara si a es mayor o igual que b
print(f"{a} <= {b} : {a <= b}")  # Compara si a es menor o igual que b

# **Operadores Lógicos**: Operadores para trabajar con valores booleanos (True o False).
print("\n🔹 Operadores lógicos con valores predefinidos:")
x = True
y = False
print(f"x and y : {x and y}")  # El operador 'and' devuelve True solo si ambos son True
print(f"x or y : {x or y}")  # El operador 'or' devuelve True si al menos uno es True
print(f"not x : {not x}")  # El operador 'not' invierte el valor booleano (True se convierte en False)

# **Operadores de Asignación**: Operadores que modifican una variable usando un valor dado.
c = int(input("\nIngresa un número entero (c): "))
print("\n🔹 Operadores de asignación aplicados a c:")
c += 2  # Suma 2 a c
print(f"c += 2 : {c}")  # Muestra el valor actualizado de c
c -= 2  # Resta 2 a c
print(f"c -= 2 : {c}")  # Muestra el valor actualizado de c
c *= 2  # Multiplica c por 2
print(f"c *= 2 : {c}")  # Muestra el valor actualizado de c
c /= 2  # Divide c entre 2
print(f"c /= 2 : {c}")  # Muestra el valor actualizado de c
c %= 2  # Asigna el residuo de c dividido entre 2
print(f"c %= 2 : {c}")  # Muestra el valor actualizado de c
c **= 2  # Eleva c al cuadrado
print(f"c **= 2 : {c}")  # Muestra el valor actualizado de c

# **Operadores de Pertenencia**: Verifica si un valor pertenece a una secuencia (como una lista).
print("\n🔹 Operadores de pertenencia en listas:")
lista = [1, 2, 3, 4, 5]  # Una lista con números
num = int(input("Ingresa un número para buscar en la lista [1,2,3,4,5]: "))
print(f"{num} in lista : {num in lista}")  # Verifica si el número está en la lista
print(f"{num} not in lista : {num not in lista}")  # Verifica si el número no está en la lista

# **Operadores de Identidad**: Compara si dos variables son el mismo objeto en memoria.
print("\n🔹 Operadores de identidad entre listas:")
x = [1, 2, 3]  # Lista con números
y = [1, 2, 3]  # Otra lista con los mismos números
z = x  # Asignamos 'x' a 'z', por lo que ambas apuntan al mismo objeto
print(f"x is y : {x is y}")  # Compara si 'x' y 'y' son el mismo objeto (False)
print(f"x is not y : {x is not y}")  # Compara si 'x' y 'y' no son el mismo objeto (True)
print(f"x is z : {x is z}")  # Compara si 'x' y 'z' son el mismo objeto (True)

# **Operador Ternario**: Es una forma corta de hacer una condición.
print("\n🔹 Uso del operador ternario para verificar si un número es positivo:")
numero = int(input("\nIngresa un número: "))
resultado = "Positivo" if numero > 0 else "Negativo o Cero"
print(f"El número es: {resultado}")  # Muestra si el número es positivo o negativo/cero
