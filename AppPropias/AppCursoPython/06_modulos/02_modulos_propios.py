# CREACIÓN Y USO DE MÓDULOS PROPIOS

# Ejemplo de módulo simple
def suma(a, b):
    """Función simple de suma"""
    return a + b

def resta(a, b):
    """Función simple de resta"""
    return a - b

# Uso de módulos propios
if __name__ == "__main__":
    print("Suma de 5 y 3:", suma(5, 3))
    print("Resta de 10 y 4:", resta(10, 4))

# CREACIÓN Y USO DE MÓDULOS PROPIOS

# En Python, un "módulo" es simplemente un archivo que contiene código Python, 
# como funciones, clases o variables, que puede ser reutilizado en otros programas.

# Definimos dos funciones simples dentro de este módulo:
def suma(a, b):
    """Función que recibe dos números y devuelve su suma."""
    return a + b


def resta(a, b):
    """Función que recibe dos números y devuelve su resta."""
    return a - b

# En Python, cada archivo .py puede ser ejecutado directamente o importado como un módulo en otro script.
# La condición "if __name__ == '__main__':" permite diferenciar estos dos usos:
# - Si el archivo se ejecuta directamente, el bloque dentro de esta condición se ejecuta.
# - Si el archivo se importa en otro script, el bloque no se ejecuta.

if __name__ == "__main__":
    # Ejemplos de uso de las funciones dentro de este módulo
    print("Ejemplo de uso del módulo propio:")
    print("Suma de 5 y 3:", suma(5, 3))  # Resultado: 8
    print("Resta de 10 y 4:", resta(10, 4))  # Resultado: 6

# Para importar este módulo en otro archivo Python, se puede hacer lo siguiente:
# Supongamos que este archivo se llama "mi_modulo.py", entonces se podría importar y usar así:
#
# import mi_modulo
# resultado = mi_modulo.suma(2, 3)
# print(resultado)  # Imprime: 5
#
# O también se pueden importar funciones específicas:
# from mi_modulo import suma, resta
# print(suma(4, 6))  # Imprime: 10
