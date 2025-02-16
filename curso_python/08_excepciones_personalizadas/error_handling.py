# GESTIÓN AVANZADA DE ERRORES

# Función para realizar una división con manejo de errores
def division_segura(a, b):
    """División con manejo de errores"""
    
    # El bloque try intenta ejecutar el código dentro de él
    try:
        # Intentamos realizar la división
        resultado = a / b
    
    # Si ocurre una excepción de tipo ZeroDivisionError (división por cero), la capturamos
    except ZeroDivisionError:
        # En caso de error, mostramos un mensaje informando sobre la división por cero
        print("Error: División por cero")
        # Retornamos None para indicar que la operación no fue exitosa
        return None
    
    # Si ocurre una excepción de tipo TypeError (tipos incompatibles para la operación), la capturamos
    except TypeError:
        # En caso de error, mostramos un mensaje informando sobre los tipos incompatibles
        print("Error: Tipos incompatibles")
        # Retornamos None para indicar que la operación no fue exitosa
        return None
    
    # Si no ocurre ningún error, ejecutamos el bloque else
    else:
        # Si la división se realizó con éxito, mostramos un mensaje indicando éxito
        print("División realizada con éxito")
        # Retornamos el resultado de la división
        return resultado
    
    # El bloque finally se ejecuta siempre, haya habido o no excepción
    finally:
        # Imprimimos un mensaje indicando que la operación de división ha finalizado
        print("Operación de división finalizada")


# Función para realizar una lectura de archivo con manejo de múltiples excepciones
def lectura_archivo_segura(ruta):
    """Lectura de archivo con múltiples excepciones"""
    
    # El bloque try intenta ejecutar el código dentro de él
    try:
        # Intentamos abrir el archivo en modo lectura ('r')
        with open(ruta, 'r') as archivo:
            # Leemos el contenido del archivo
            contenido = archivo.read()
            # Retornamos el contenido del archivo
            return contenido
    
    # Si ocurre una excepción de tipo FileNotFoundError (el archivo no existe), la capturamos
    except FileNotFoundError:
        # Si el archivo no se encuentra, mostramos un mensaje indicando este error
        print(f"Archivo no encontrado: {ruta}")
    
    # Si ocurre una excepción de tipo PermissionError (no se tienen permisos para leer el archivo), la capturamos
    except PermissionError:
        # Si no se tienen permisos para leer el archivo, mostramos un mensaje indicando este error
        print(f"Sin permisos para leer: {ruta}")
    
    # Si ocurre una excepción de tipo IsADirectoryError (la ruta es un directorio y no un archivo), la capturamos
    except IsADirectoryError:
        # Si la ruta es un directorio, mostramos un mensaje indicando este error
        print(f"La ruta es un directorio: {ruta}")
    
    # Capturamos cualquier otra excepción no especificada por las anteriores
    except Exception as e:
        # En caso de cualquier otro error inesperado, mostramos el mensaje de error
        print(f"Error inesperado: {e}")


# El bloque principal donde se ejecutan las funciones para realizar pruebas
if __name__ == "__main__":
    # Llamamos a la función division_segura con dos números válidos (10 y 2)
    division_segura(10, 2)
    # Llamamos a la función division_segura con el segundo número como 0 (causará una excepción)
    division_segura(10, 0)
    
    # Llamamos a la función lectura_archivo_segura con una ruta que no existe (causará un FileNotFoundError)
    lectura_archivo_segura("archivo_inexistente.txt")
    # Llamamos a la función lectura_archivo_segura con una ruta que es un directorio (causará un IsADirectoryError)
    lectura_archivo_segura("/")
