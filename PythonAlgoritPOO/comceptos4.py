# IBM SkillsBuild | Introducción a Python
# Conceptos básicos y sintaxis de Python

# VARIABLES
# Lo ideal es declarar e inicializar siempre las variables

# Asignación de variable a otra variable
var = "Hola mundo"
var2 = var
print(var2)  # Imprime: Hola mundo
# var y var2 apuntan a la misma cadena de texto

# REGLAS DE NOMBRES DE VARIABLES
# Pueden contener:
# - Letras mayúsculas y minúsculas (A-Z, a-z)
# - Dígitos (0-9)
# - Carácter de subrayado (_)

# EJEMPLOS NO VÁLIDOS (generarán error)
# var& = "Hola mundo"  # Caracteres especiales no permitidos
# 2var = "Hola mundo"  # No puede empezar con número

# SENSIBILIDAD A MAYÚSCULAS
Var3 = "Hola mundo"
# print(var3)  # Generaría error si var3 no está definida

# DECLARACIÓN DE VARIABLES
n_edad = 47  # Variable numérica entera
n_numero = -23.5245  # Variable numérica de coma flotante
s_nombre = 'Manolo es "amigo" mío'  # Variable de texto

# String multilínea
s_textoLargo = """Esto es un mensaje 
...con tres saltos 
...de linea"""

# Sobreescritura de variable
s_edad = "47"

# Declaración de constante
NUMEROPI = 3.14159

# Variables booleanas
is_verdadero = True
is_casado = False

# Equivalencias booleanas
print(True == 1)  # True
print(False == 0)  # True
print(True + 2)  # 3

# Validación de condiciones
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

# Declaración múltiple de variables
a, b, c = 'string', 15, True

# VERIFICACIÓN DE TIPOS
print(type(n_edad))
print(type(n_numero))
print(type(s_nombre))
print(type(NUMEROPI))
print(type(is_verdadero))
print(type(is_casado))

# CASTING (FORZADO DE TIPOS)
# Enteros
x = int(1)       # x valdrá 1
y = int(2.8)     # y valdrá 2
z = int("3")     # z valdrá 3

# Float
x_float = float(1)       # x valdrá 1.0
y_float = float(2.8)     # y valdrá 2.8
z_float = float("3")     # z valdrá 3.0
w_float = float("4.2")   # w valdrá 4.2

# String
x_str = str("s1")    # x valdrá 's1'
y_str = str(2)       # y valdrá '2'
z_str = str(3.0)     # z valdrá '3.0'

# Reconversión de tipos
n_numero = 13
n_numero_2 = float(n_numero)

n_numero_3 = 24.876
n_numero_4 = int(n_numero_3)

s_texto = "13"
n_numero_5 = int(s_texto)

n_numero_6 = 27
s_texto_2 = str(n_numero_6)

# Imprimir resultados de casting
print(n_numero_2)
print(type(n_numero_2))
print(n_numero_4)
print(type(n_numero_4))
print(n_numero_5)
print(type(n_numero_5))
print(s_texto_2)
print(type(s_texto_2))

# COMENTARIOS
# Los comentarios son anotaciones que el programa no tiene en cuenta
# Tipos de comentarios:
# Comentario de una línea
"""Comentario 
de 
varias líneas"""

# MÉTODOS DE STRINGS
# Concatenación
print("Esta frase", "termina aquí.")  # Con coma (añade espacio)
print("Esta frase " + "termina aquí.")  # Con +

# Concatenación y multiplicación
a = "uno"
b = "dos"
c = a + b    # c es "unodos"
c = a * 3    # c es "unounouno"

# Métodos de strings
# lower(): Convierte a minúsculas
s_texto1 = "ESTE TEXTO ESTÁ INICIALMENTE EN MAYÚSCULAS"
print(s_texto1.lower())

# capitalize(): Primera letra en mayúscula
s_texto2 = "este texto no tenía la primera letra en mayúsculas"
print(s_texto2.capitalize())

# count(): Cuenta apariciones de letra/cadena
s_texto3 = "Vamos a ver cuántas veces aparece la letra c"
print(s_texto3.count('c'))

# find(): Posición primera aparición
s_texto4 = "Vamos a ver en qué posición aparece primero la letra e"
print(s_texto4.find('e'))

# rfind(): Busca desde el final
s_texto5 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print(s_texto5.rfind('desde'))

# isdigit(): Comprueba si es dígito
s_texto6 = "6"
print(s_texto6.isdigit())

# isalnum(): Comprueba si es alfanumérico
s_texto7 = "9857654gf7"
print(s_texto7.isalnum())

# isalpha(): Comprueba si son solo letras
s_texto8 = "Holamundo"
print(s_texto8.isalpha())

# split(): Separa por palabras
s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split())

# split() con separador personalizado
s_texto10 = "Esta sería la primera parte,y esta la segunda"
print(s_texto10.split(","))

# strip(): Elimina espacios inicio/final
s_texto11 = " En este texto había espacios al principio y al final "
print(s_texto11.strip())

# replace(): Reemplaza texto
s_texto12 = "Vamos reemplazar la palabra casa"
print(s_texto12.replace("casa", "hogar"))

# SALIDA DE DATOS (print())
# Salida directa
print("En esta ocasión hemos imprimido por pantalla este string")

# Salida de datos calculados
n_numero_1 = 4
n_numero_2 = 6
print("El resultado de sumar", n_numero_1, "y", n_numero_2, "es", (n_numero_1+n_numero_2))

# ENTRADA DE DATOS (input())
s_nombreIntroducido = input("Introduzca su nombre: ")
print("Bienvenido", s_nombreIntroducido)

# IMPORTANTE: input() devuelve siempre un string
s_edad = int(input("Introduzca su edad: "))
print("El año que viene tendrá usted", s_edad + 1, "años")

# OPERADORES
# Módulo (resto de división)
n_numerador = 85
n_denominador = 9
n_resto = n_numerador % n_denominador
print("El resto de dividir", n_numerador, "entre", n_denominador, "es", n_resto)

# Operadores de comparación
n_numero1 = 34
s_texto1 = "34"
n_numero1 == s_texto1  # Comparación

n_numero2 = 34
n_numero3 = 34
n_numero2 == n_numero3  # True

# Operador != (diferente)
n_numero4 = 34
n_numero5 = 34
n_numero4 != n_numero5

# Operador += (suma e incremento)
n_numero6 = 34
n_numero6 += 1  # Equivalente a n_numero6 = n_numero6 + 1
print(n_numero6)

# OPERADORES LÓGICOS
a = True
b = False
resultado = a and b
resultado = a or b
resultado = not a
print(resultado)

# Sintaxis de operadores lógicos
edad = int(input('Introduce tu edad: '))
if (20 <= edad < 30) or (30 <= edad < 40):
    print('Dentro de rango (20\'s) o (30\'s)')
else:
    print("No está dentro de los 20's ni 30's")

# OBJETOS MUTABLES E INMUTABLES
# Dirección de memoria
a = 65
print("Dirección de memoria:", id(a))

# Variable apuntando a otra
miNumero = 65
miNumero2 = miNumero
print("Dirección miNumero:", id(miNumero))
print("Dirección miNumero2:", id(miNumero2))

# Cambio de variable
a = 65
print("Dirección inicial:", id(a))
a += 2
print("Dirección después de modificar:", id(a))

# Direcciones de memoria de diferentes tipos
# Tupla
a = (1, 2, 3, 4, 5)
print("Dirección de tupla:", id(a))

# Lista
a = [1, 2, 3, 4, 5]
print("Dirección de lista:", id(a))

# Diccionario
a = {'a': 1, 'b': 2}
print("Dirección inicial de diccionario:", id(a))
a["c"] = 3
print("Diccionario modificado:", a)
print("Dirección después de modificar:", id(a))

