# ESTRUCTURAS CONDICIONALES EN PYTHON
# ======================================
# Objetivo: Proporcionar una guía completa sobre las estructuras condicionales en Python.
# Este archivo cubre las estructuras if simples, if-else, if-elif-else, operadores lógicos y el operador ternario.

# 1. If Simple: Se utiliza para evaluar una única condición.
# Solicitamos la edad del usuario y la almacenamos como un entero.
edad = int(input("🔹 Ingresa tu edad: "))  # Convertimos la entrada a entero.
if edad >= 18:  # Condición: la edad es mayor o igual a 18
    print("Eres mayor de edad")  # Mensaje si la condición es verdadera

# 2. If-else: Permite evaluar dos condiciones, una para cuando la condición es verdadera y otra cuando es falsa.
if edad >= 18:  # Si la edad es mayor o igual a 18
    print("Puedes votar")  # Mensaje si la condición es verdadera
else:  # Si la condición anterior es falsa
    print("No puedes votar")  # Mensaje si la condición es falsa

# 3. If-elif-else: Se usa cuando necesitamos evaluar múltiples condiciones.
# Solicitamos la nota del usuario y la almacenamos como un entero.
nota = int(input("🔹 Ingresa tu nota: "))  # Convertimos la entrada a entero.
# Evaluamos la nota y asignamos la calificación correspondiente.
if nota >= 90:  # Si la nota es mayor o igual a 90
    calificacion = "A"  # Calificación A
elif nota >= 80:  # Si la nota no es mayor o igual a 90, pero es mayor o igual a 80
    calificacion = "B"  # Calificación B
elif nota >= 70:  # Si la nota no es mayor o igual a 80, pero es mayor o igual a 70
    calificacion = "C"  # Calificación C
else:  # Si la nota es menor a 70
    calificacion = "F"  # Calificación F

# Imprimimos la calificación final.
print(f"Tu calificación es: {calificacion}")  # Muestra la calificación del estudiante.

# 4. Operadores Lógicos: Permiten combinar condiciones para realizar comparaciones más complejas.
# Definimos variables para verificar condiciones.
tiene_credencial = True  # Suponemos que la persona tiene una credencial
edad_valida = edad >= 18  # Verificamos si la persona es mayor o igual a 18

# Usamos el operador lógico "and" para verificar que ambas condiciones sean verdaderas.
if tiene_credencial and edad_valida:
    print("Puedes entrar")  # Mensaje si ambas condiciones son verdaderas

# 5. Operador Ternario: Es una forma compacta de realizar un condicional en una sola línea.
estado = "Aprobado" if nota >= 70 else "Reprobado"  # Verificamos la nota para determinar el estado.

# Imprimimos el estado del estudiante.
print(f"Estado: {estado}")  # Muestra si el estudiante está aprobado o reprobado.

# EJERCICIOS FINALES
# ======================================
print("\n🔹 Ejercicios Finales:")

# Ejercicio 1: Preguntar al usuario por dos números, realizar una operación y mostrar el resultado.
try:
    numero1 = int(input("Ingresa el primer número: "))  # Solicita un número y lo convierte a entero.
    numero2 = int(input("Ingresa el segundo número: "))  # Solicita otro número y lo convierte a entero.
    if numero1 > numero2:
        print(f"{numero1} es mayor que {numero2}.")
    elif numero1 < numero2:
        print(f"{numero1} es menor que {numero2}.")
    else:
        print(f"{numero1} es igual a {numero2}.")
except ValueError:
    print("❌ Error: ¡Por favor, ingresa solo números enteros!")

# Ejercicio 2: Usar el operador ternario para verificar si un número es positivo, negativo o cero.
numero_verificacion = int(input("Ingresa un número para verificar: "))  # Solicita un número.
resultado = "Positivo" if numero_verificacion > 0 else "Negativo" if numero_verificacion < 0 else "Cero"  # Evaluación.
print(f"El número {numero_verificacion} es: {resultado}")  # Muestra el resultado.

# GLOSARIO
# ======================================
print("""
📖 Glosario:
- Estructura condicional: Permite ejecutar bloques de código dependiendo de ciertas condiciones.
- If: Estructura que evalúa una condición y ejecuta un bloque de código si es verdadera.
- Else: Bloque que se ejecuta si la condición de 'if' es falsa.
- Elif: Permite evaluar una nueva condición si las anteriores fueron falsas.
- Operador lógico: Combina condiciones para obtener un resultado booleano (True o False).
- Operador ternario: Forma compacta de una estructura condicional que devuelve un valor basado en una condición.
""")