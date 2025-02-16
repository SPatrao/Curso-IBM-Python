# MANEJO DE ARCHIVOS EN PYTHON

# Modos de apertura de archivos:
# 'r': Lectura (defecto)
# 'w': Escritura (sobrescribe)
# 'a': Añadir al final
# 'r+': Lectura y escritura
# 'b': Modo binario

def leer_archivo_texto():
    """Leer archivo de texto completo"""
    try:
        with open('ejemplo.txt', 'r') as archivo:
            contenido = archivo.read()
            print("Contenido completo:", contenido)
    except FileNotFoundError:
        print("Archivo no encontrado")

def leer_lineas_archivo():
    """Leer archivo línea por línea"""
    try:
        with open('ejemplo.txt', 'r') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("Archivo no encontrado")

def escribir_archivo():
    """Escribir en un archivo"""
    with open('nuevo_archivo.txt', 'w') as archivo:
        archivo.write("Hola mundo\n")
        archivo.write("Esto es una prueba de escritura")

def añadir_archivo():
    """Añadir contenido a un archivo existente"""
    with open('nuevo_archivo.txt', 'a') as archivo:
        archivo.write("\nNueva línea añadida")

def leer_binario():
    """Leer archivo en modo binario"""
    try:
        with open('imagen.jpg', 'rb') as archivo:
            contenido = archivo.read()
            print(f"Tamaño del archivo: {len(contenido)} bytes")
    except FileNotFoundError:
        print("Archivo binario no encontrado")

if __name__ == "__main__":
    # Ejemplos de uso
    escribir_archivo()
    leer_archivo_texto()
    añadir_archivo()

