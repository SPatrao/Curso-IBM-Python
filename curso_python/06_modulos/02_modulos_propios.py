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

