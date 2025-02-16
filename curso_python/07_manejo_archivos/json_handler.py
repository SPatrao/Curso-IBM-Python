# MANEJO DE ARCHIVOS JSON
# Este archivo demuestra cómo trabajar con archivos JSON en Python:
# 1. Escribir un archivo JSON.
# 2. Leer un archivo JSON.
# 3. Modificar el contenido de un archivo JSON existente.
# El formato JSON (JavaScript Object Notation) es un formato ligero de intercambio de datos y es muy utilizado para el almacenamiento y la transmisión de datos en aplicaciones web.

import json  # Importamos la librería json que permite convertir objetos Python a formato JSON y viceversa.

# Función para escribir datos en un archivo JSON
def escribir_json():
    """
    Esta función escribe un conjunto de datos en formato JSON en un archivo llamado 'datos.json'.
    Los datos se representan como un diccionario de Python, que luego se convierte a formato JSON.
    """
    # Definimos un diccionario de Python con algunos datos de ejemplo que vamos a convertir a JSON.
    # El diccionario contiene:
    # - 'nombre': un string que representa el nombre de una persona.
    # - 'edad': un entero que representa la edad de la persona.
    # - 'ciudad': un string que representa la ciudad de residencia.
    # - 'cursos': una lista que contiene varios strings representando los cursos que la persona ha tomado.
    datos = {
        "nombre": "Juan Pérez",  # Nombre de la persona.
        "edad": 30,              # Edad de la persona.
        "ciudad": "Madrid",      # Ciudad donde vive.
        "cursos": ["Python", "Data Science", "Machine Learning"]  # Lista de cursos que ha tomado.
    }
    
    # Abrimos el archivo 'datos.json' en modo escritura ('w'). Si el archivo no existe, se crea automáticamente.
    with open('datos.json', 'w') as archivo:
        # Usamos la función json.dump() para convertir el diccionario 'datos' a formato JSON.
        # El argumento 'indent=4' hace que el JSON sea legible al agregar indentación de 4 espacios.
        # El contenido del diccionario se guarda en el archivo como un archivo JSON.
        json.dump(datos, archivo, indent=4)

# Función para leer datos desde un archivo JSON
def leer_json():
    """
    Esta función lee un archivo JSON llamado 'datos.json', carga los datos en un diccionario de Python
    y los imprime de manera legible en formato JSON.
    """
    try:
        # Intentamos abrir el archivo 'datos.json' en modo lectura ('r').
        # Si el archivo existe, lo cargamos y mostramos su contenido.
        with open('datos.json', 'r') as archivo:
            # Usamos json.load() para leer el archivo y convertir el contenido JSON en un diccionario de Python.
            # 'datos' será un diccionario con la misma estructura que definimos en la función escribir_json.
            datos = json.load(archivo)
            
            # Imprimimos los datos leídos desde el archivo en formato JSON, con una indentación de 2 espacios.
            print("Datos leídos:")
            print(json.dumps(datos, indent=2))  # Convertimos el diccionario a formato JSON con indentación para mostrarlo.
    except FileNotFoundError:
        # Si el archivo 'datos.json' no se encuentra, capturamos el error y mostramos un mensaje.
        print("Archivo JSON no encontrado")

# Función para modificar los datos en un archivo JSON
def modificar_json():
    """
    Esta función lee un archivo JSON, agrega un nuevo campo al diccionario de datos
    y guarda los cambios en el mismo archivo.
    """
    try:
        # Intentamos abrir el archivo 'datos.json' en modo lectura y escritura ('r+').
        # El modo 'r+' permite leer y escribir en el archivo, pero no lo sobrescribe desde el principio.
        with open('datos.json', 'r+') as archivo:
            # Leemos el contenido actual del archivo y lo convertimos en un diccionario Python.
            datos = json.load(archivo)
            
            # Modificamos el diccionario agregando un nuevo campo. En este caso, añadimos un nuevo campo 'nuevo_campo'.
            # Este campo tiene como valor un string "Valor añadido".
            datos['nuevo_campo'] = "Valor añadido"  # Añadimos un nuevo par clave-valor al diccionario.
            
            # Usamos 'seek(0)' para mover el puntero del archivo al principio, de modo que podamos sobrescribir el archivo desde el inicio.
            archivo.seek(0)
            
            # Escribimos el diccionario modificado en el archivo, convirtiéndolo de nuevo a formato JSON.
            # 'indent=4' asegura que el archivo resultante tenga una indentación de 4 espacios.
            json.dump(datos, archivo, indent=4)
            
            # Usamos 'truncate()' para borrar cualquier contenido restante en el archivo que no haya sido sobrescrito.
            # Esto es útil en caso de que el nuevo contenido sea más corto que el anterior.
            archivo.truncate()
    except FileNotFoundError:
        # Si el archivo 'datos.json' no se encuentra, capturamos el error y mostramos un mensaje.
        print("Archivo JSON no encontrado")

# Bloque principal que se ejecuta si este archivo se ejecuta directamente
if __name__ == "__main__":
    """
    El bloque if __name__ == "__main__": asegura que el código dentro de este bloque solo se ejecute
    cuando el archivo se ejecute directamente, y no cuando se importe como módulo en otro archivo.
    """
    
    # Llamamos a la función escribir_json() para crear un archivo 'datos.json' con los datos iniciales.
    escribir_json()
    
    # Llamamos a la función leer_json() para leer y mostrar los datos desde el archivo 'datos.json'.
    leer_json()
    
    # Llamamos a la función modificar_json() para agregar un nuevo campo al archivo 'datos.json'.
    modificar_json()
