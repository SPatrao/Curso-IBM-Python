# Importación de módulos necesarios para la ejecución del código.
import os  # Proporciona una forma de interactuar con el sistema operativo, como la gestión de archivos y directorios.
import importlib  # Utilizado para importar módulos de forma dinámica en tiempo de ejecución.
import importlib.util  # Herramientas auxiliares para gestionar la importación dinámica de módulos.

# Diccionario de rutas de módulos actualizado
# Cada categoría (clave) tiene una lista de archivos (valores) que representan los módulos disponibles.
MODULOS = {
    '01_introduccion': [
        '01_variables.py',  # Módulo que cubre las variables en Python.
        '02_tipos_datos.py',  # Módulo que cubre los tipos de datos en Python.
        '03_operadores.py'  # Módulo que cubre los operadores en Python.
    ],
    '02_estructuras_control': [
        '01_condicionales.py',  # Módulo que cubre estructuras de control condicional (if, else).
        '02_bucles.py',  # Módulo que cubre los bucles (for, while).
        '03_excepciones.py'  # Módulo que cubre el manejo de excepciones.
    ],
    # Otras categorías y módulos siguen una estructura similar.
}

def limpiar_pantalla():
    """Función para limpiar la pantalla dependiendo del sistema operativo.
    En sistemas Windows (nt) ejecuta 'cls' y en otros sistemas ejecuta 'clear'."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Ejecuta el comando adecuado para limpiar la pantalla.

def mostrar_menu_principal():
    """Muestra el menú principal con las categorías de módulos disponibles.
    Permite al usuario seleccionar una categoría para ver los módulos dentro de ella."""
    limpiar_pantalla()  # Limpiar la pantalla antes de mostrar el menú.
    print("=== MENÚ PRINCIPAL DE PYTHON ===")
    # Recorre las categorías y módulos disponibles en el diccionario MODULOS, 
    # mostrando las categorías numeradas.
    for i, (categoria, modulos) in enumerate(MODULOS.items(), 1):
        print(f"{i}. {categoria}")  # Muestra la categoría.
    print("0. Salir")  # Opción para salir del programa.
    return input("Seleccione una categoría: ")  # Devuelve la opción seleccionada por el usuario.

def mostrar_modulos(categoria):
    """Muestra los módulos de una categoría seleccionada.
    Permite al usuario elegir un módulo dentro de la categoría especificada."""
    limpiar_pantalla()  # Limpiar la pantalla antes de mostrar los módulos.
    modulos = MODULOS[categoria]  # Obtiene la lista de módulos de la categoría seleccionada.
    print(f"=== MÓDULOS DE {categoria.upper()} ===")
    # Muestra cada módulo de la categoría numerado.
    for i, modulo in enumerate(modulos, 1):
        print(f"{i}. {modulo}")  # Muestra el nombre del módulo.
    print("0. Volver al menú principal")  # Opción para volver al menú principal.
    return input("Seleccione un módulo: ")  # Devuelve la opción seleccionada por el usuario.

def ejecutar_modulo(categoria, modulo):
    """Ejecuta un módulo seleccionado de una categoría específica.
    Importa dinámicamente el módulo y lo ejecuta."""
    try:
        limpiar_pantalla()  # Limpiar la pantalla antes de ejecutar el módulo.
        # Construye la ruta completa del archivo del módulo a partir del directorio actual y la categoría.
        ruta_completa = os.path.join(os.getcwd(), "curso_python", categoria, modulo)
        
        # Verifica si el archivo del módulo existe en la ruta especificada.
        if not os.path.exists(ruta_completa):
            print(f"Error: El archivo {modulo} no existe en {categoria}")
            input("Presione Enter para continuar...")  # Pausa para que el usuario lea el error.
            return
        
        # Carga dinámicamente el módulo especificado usando importlib.
        spec = importlib.util.spec_from_file_location(modulo, ruta_completa)
        modulo_importado = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo_importado)  # Ejecuta el módulo importado.
        
    except Exception as e:
        print(f"Error al ejecutar el módulo {modulo}: {e}")  # Si ocurre un error, lo muestra.
    
    input("\nPresione Enter para continuar...")  # Pausa después de ejecutar el módulo.

def main():
    """Función principal que gestiona el flujo de ejecución del menú.
    Permite navegar entre categorías y módulos hasta ejecutar el programa."""
    while True:
        opcion_categoria = mostrar_menu_principal()  # Muestra el menú principal y obtiene la categoría seleccionada.
        
        if opcion_categoria == '0':
            break  # Si el usuario selecciona '0', sale del programa.
        
        try:
            categoria_seleccionada = list(MODULOS.keys())[int(opcion_categoria) - 1]  # Obtiene la categoría seleccionada.
            
            while True:
                opcion_modulo = mostrar_modulos(categoria_seleccionada)  # Muestra los módulos de la categoría seleccionada.
                
                if opcion_modulo == '0':
                    break  # Si el usuario selecciona '0', vuelve al menú principal.
                
                try:
                    # Obtiene el módulo seleccionado y lo ejecuta.
                    modulo_seleccionado = MODULOS[categoria_seleccionada][int(opcion_modulo) - 1]
                    ejecutar_modulo(categoria_seleccionada, modulo_seleccionado)  # Ejecuta el módulo seleccionado.
                except (ValueError, IndexError):
                    print("Opción de módulo inválida")  # Si la opción del módulo es inválida, muestra un mensaje de error.
                    input("Presione Enter para continuar...")  # Pausa para que el usuario vea el mensaje.

        except (ValueError, IndexError):
            print("Categoría inválida")  # Si la categoría seleccionada es inválida, muestra un mensaje de error.
            input("Presione Enter para continuar...")  # Pausa para que el usuario vea el mensaje.

def crear_estructura_directorios():
    """Crea los directorios correspondientes si no existen.
    Crea un directorio por cada categoría para organizar los módulos."""
    directorios = list(MODULOS.keys())  # Obtiene una lista con los nombres de las categorías.
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)  # Crea el directorio si no existe.
            print(f"Creado directorio: {directorio}")  # Muestra un mensaje indicando que se ha creado el directorio.

if __name__ == "__main__":
    # Antes de ejecutar el menú, asegura que los directorios estén creados.
    crear_estructura_directorios()  
    
    # Ejecuta el flujo principal del programa, mostrando el menú y permitiendo la selección de módulos.
    main()
