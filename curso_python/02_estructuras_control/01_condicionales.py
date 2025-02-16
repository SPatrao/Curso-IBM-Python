# ESTRUCTURAS CONDICIONALES EN PYTHON

# 1. If simple: se utiliza para evaluar una única condición.
edad = int(input("🔹 Ingresa tu edad: "))
if edad >= 18:  # Si la edad es mayor o igual a 18
    print("Eres mayor de edad")  # Se ejecuta esta línea si la condición es verdadera

# 2. If-else: permite evaluar dos condiciones, una para cuando la condición es verdadera y otra cuando es falsa.
if edad >= 18:  # Si la edad es mayor o igual a 18
    print("Puedes votar")  # Se ejecuta esta línea si la condición es verdadera
else:  # Si la condición anterior es falsa
    print("No puedes votar")  # Se ejecuta esta línea si la condición es falsa

# 3. If-elif-else: se usa cuando necesitamos evaluar múltiples condiciones.
nota = 85
if nota >= 90:  # Si la nota es mayor o igual a 90
    calificacion = "A"  # Asignamos la calificación A
elif nota >= 80:  # Si la nota no es mayor o igual a 90, pero es mayor o igual a 80
    calificacion = "B"  # Asignamos la calificación B
elif nota >= 70:  # Si la nota no es mayor o igual a 80, pero es mayor o igual a 70
    calificacion = "C"  # Asignamos la calificación C
else:  # Si la nota no cumple con ninguna de las condiciones anteriores (es menor a 70)
    calificacion = "F"  # Asignamos la calificación F

# Imprimimos la calificación final
print(f"Tu calificación es: {calificacion}")

# 4. Operadores lógicos: permiten combinar condiciones para realizar comparaciones más complejas.
tiene_credencial = True  # Suponemos que la persona tiene credencial
edad_valida = edad >= 18  # Comprobamos si la persona es mayor o igual a 18

# Usamos el operador lógico "and" para verificar que ambas condiciones sean verdaderas.
if tiene_credencial and edad_valida:
    print("Puedes entrar")  # Si ambas condiciones son verdaderas, se ejecuta esta línea

# 5. Operador ternario: es una forma compacta de realizar un condicional en una sola línea.
estado = "Aprobado" if nota >= 70 else "Reprobado"  # Si la nota es mayor o igual a 70, el estado es "Aprobado", si no, es "Reprobado".

# Imprimimos el estado del estudiante
print(f"Estado: {estado}")
