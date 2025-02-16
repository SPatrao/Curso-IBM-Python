# GESTIÓN AVANZADA DE ERRORES

def division_segura(a, b):
    """División con manejo de errores"""
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    except TypeError:
        print("Error: Tipos incompatibles")
        return None
    else:
        print("División realizada con éxito")
        return resultado
    finally:
        print("Operación de división finalizada")

def lectura_archivo_segura(ruta):
    """Lectura de archivo con múltiples excepciones"""
    try:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
    except PermissionError:
        print(f"Sin permisos para leer: {ruta}")
    except IsADirectoryError:
        print(f"La ruta es un directorio: {ruta}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    division_segura(10, 2)
    division_segura(10, 0)
    
    lectura_archivo_segura("archivo_inexistente.txt")
    lectura_archivo_segura("/")

