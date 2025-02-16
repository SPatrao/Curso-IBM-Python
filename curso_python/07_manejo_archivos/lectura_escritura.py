# MANEJO DE ARCHIVOS EN PYTHON

# Los modos de apertura de archivos determinan cómo se accede al archivo.
# 'r' -> Lectura (es el modo predeterminado): Permite leer el contenido de un archivo.
# 'w' -> Escritura: Crea un nuevo archivo o sobrescribe el archivo existente.
# 'a' -> Añadir: Permite añadir contenido al final del archivo sin sobrescribir.
# 'r+' -> Lectura y escritura: Permite tanto leer como escribir en el archivo.
# 'b' -> Modo binario: Abre el archivo en formato binario, necesario para archivos no-textuales (como imágenes).

def leer_archivo_texto():
    """
    Leer archivo de texto completo.
    
    Este método abre un archivo en modo de lectura ('r') y lee su contenido completo.
    El contenido del archivo se imprime en la consola.
    Si el archivo no se encuentra, se maneja la excepción FileNotFoundError.
    
    Ejemplo de uso:
        leer_archivo_texto()
    """
    try:
        # Abrimos el archivo 'ejemplo.txt' en modo lectura ('r').
        with open('ejemplo.txt', 'r') as archivo:
            # Leemos todo el contenido del archivo con 'read()'.
            contenido = archivo.read()
            # Imprimimos el contenido completo en la consola.
            print("Contenido completo:", contenido)
    except FileNotFoundError:
        # Si el archivo no se encuentra, mostramos un mensaje de error.
        print("Archivo no encontrado")

def leer_lineas_archivo():
    """
    Leer archivo línea por línea.
    
    Este método abre un archivo en modo lectura ('r') y lee el archivo línea por línea,
    imprimiendo cada línea sin los saltos de línea adicionales.
    
    Ejemplo de uso:
        leer_lineas_archivo()
    """
    try:
        # Abrimos el archivo 'ejemplo.txt' en modo lectura ('r').
        with open('ejemplo.txt', 'r') as archivo:
            # Iteramos sobre cada línea del archivo usando un bucle 'for'.
            for linea in archivo:
                # Usamos 'strip()' para eliminar los saltos de línea.
                print(linea.strip())
    except FileNotFoundError:
        # Si el archivo no se encuentra, mostramos un mensaje de error.
        print("Archivo no encontrado")

def escribir_archivo():
    """
    Escribir en un archivo.
    
    Este método abre un archivo en modo escritura ('w'). Si el archivo no existe, 
    se crea. Si ya existe, su contenido será sobrescrito.
    Escribe dos líneas de texto en el archivo 'nuevo_archivo.txt'.
    
    Ejemplo de uso:
        escribir_archivo()
    """
    # Abrimos el archivo 'nuevo_archivo.txt' en modo escritura ('w').
    with open('nuevo_archivo.txt', 'w') as archivo:
        # Escribimos dos líneas de texto en el archivo usando 'write()'.
        archivo.write("Hola mundo\n")
        archivo.write("Esto es una prueba de escritura")

def añadir_archivo():
    """
    Añadir contenido a un archivo existente.
    
    Este método abre un archivo en modo añadir ('a'). Si el archivo no existe, 
    se crea. Si existe, el nuevo contenido se añade al final del archivo.
    Añade una nueva línea de texto al archivo 'nuevo_archivo.txt'.
    
    Ejemplo de uso:
        añadir_archivo()
    """
    # Abrimos el archivo 'nuevo_archivo.txt' en modo añadir ('a').
    with open('nuevo_archivo.txt', 'a') as archivo:
        # Añadimos una nueva línea al final del archivo con 'write()'.
        archivo.write("\nNueva línea añadida")

def leer_binario():
    """
    Leer archivo en modo binario.
    
    Este método abre un archivo en modo binario ('rb') y lee su contenido.
    El tamaño del archivo se imprime en la consola, en lugar de leer el contenido textual.
    Si el archivo no se encuentra, se maneja la excepción FileNotFoundError.
    
    Ejemplo de uso:
        leer_binario()
    """
    try:
        # Abrimos el archivo 'imagen.jpg' en modo binario ('rb').
        with open('imagen.jpg', 'rb') as archivo:
            # Leemos todo el contenido del archivo binario con 'read()'.
            contenido = archivo.read()
            # Imprimimos el tamaño del archivo en bytes.
            print(f"Tamaño del archivo: {len(contenido)} bytes")
    except FileNotFoundError:
        # Si el archivo no se encuentra, mostramos un mensaje de error.
        print("Archivo binario no encontrado")

# Esta sección del código ejecuta los métodos para demostrar su funcionalidad.
if __name__ == "__main__":
    # Ejemplo de uso de los métodos definidos
    escribir_archivo()  # Llamada para escribir en un archivo
    leer_archivo_texto()  # Llamada para leer el archivo completo
    añadir_archivo()  # Llamada para añadir contenido al archivo existente
