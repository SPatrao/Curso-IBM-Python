import os
import importlib
import importlib.util

# Diccionario de rutas de módulos ACTUALIZADO
MODULOS = {
    '01_introduccion': [
        '01_variables.py',
        '02_tipos_datos.py', 
        '03_operadores.py'
    ],
    '02_estructuras_control': [
        '01_condicionales.py',
        '02_bucles.py', 
        '03_excepciones.py'
    ],
    '03_funciones': [
        '01_definicion.py',
        '02_argumentos.py',
        '03_lambda.py'
    ],
    '04_estructura_datos': [
        '01_listas.py',
        '02_tuplas.py',
        '03_diccionarios.py', 
        '04_sets.py'
    ],
    '05_poo': [
        '01_clases.py',
        '02_herencia.py',
        '03_polimorfismo.py'
    ],
    '06_modulos': [
        '01_modulos_nativos.py',
        '02_modulos_propios.py'
    ],
    '07_manejo_archivos': [
        'lectura_escritura.py',
        'csv_handler.py',
        'json_handler.py'
    ],
    '08_excepciones_personalizadas': [
        'custom_exceptions.py',
        'error_handling.py'
    ],
    '09_decoradores': [
        'basic_decorators.py',
        'advanced_decorators.py'
    ],
    '10_generadores': [
        'generadores_basicos.py',
        'generadores_avanzados.py'
    ],
    '11_programacion_funcional': [
        'map_filter_reduce.py',
        'funciones_orden_superior.py'
    ]
}

def limpiar_pantalla():
    """Limpiar la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    """Mostrar menú principal de módulos"""
    limpiar_pantalla()
    print("=== MENÚ PRINCIPAL DE PYTHON ===")
    for i, (categoria, modulos) in enumerate(MODULOS.items(), 1):
        print(f"{i}. {categoria}")
    print("0. Salir")
    return input("Seleccione una categoría: ")

def mostrar_modulos(categoria):
    """Mostrar módulos de una categoría"""
    limpiar_pantalla()
    modulos = MODULOS[categoria]
    print(f"=== MÓDULOS DE {categoria.upper()} ===")
    for i, modulo in enumerate(modulos, 1):
        print(f"{i}. {modulo}")
    print("0. Volver al menú principal")
    return input("Seleccione un módulo: ")

def ejecutar_modulo(categoria, modulo):
    """Ejecutar un módulo específico"""
    try:
        # Construir ruta completa del módulo
        limpiar_pantalla()
        ruta_completa = os.path.join(os.getcwd(), "curso_python", categoria, modulo)
        
        # Verificar si el archivo existe
        if not os.path.exists(ruta_completa):
            print(f"Error: El archivo {modulo} no existe en {categoria}")
            input("Presione Enter para continuar...")
            return
        
        # Importar y ejecutar módulo
        spec = importlib.util.spec_from_file_location(modulo, ruta_completa)
        modulo_importado = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo_importado)
        
    except Exception as e:
        print(f"Error al ejecutar el módulo {modulo}: {e}")
    
    input("\nPresione Enter para continuar...")

def main():
    while True:
        opcion_categoria = mostrar_menu_principal()
        
        if opcion_categoria == '0':
            break
        
        try:
            categoria_seleccionada = list(MODULOS.keys())[int(opcion_categoria) - 1]
            
            while True:
                opcion_modulo = mostrar_modulos(categoria_seleccionada)
                
                if opcion_modulo == '0':
                    break
                
                try:
                    modulo_seleccionado = MODULOS[categoria_seleccionada][int(opcion_modulo) - 1]
                    ejecutar_modulo(categoria_seleccionada, modulo_seleccionado)
                except (ValueError, IndexError):
                    print("Opción de módulo inválida")
                    input("Presione Enter para continuar...")
        
        except (ValueError, IndexError):
            print("Categoría inválida")
            input("Presione Enter para continuar...")

def crear_estructura_directorios():
    """Crear estructura de directorios si no existe"""
    directorios = list(MODULOS.keys())
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f"Creado directorio: {directorio}")

if __name__ == "__main__":
    # Crear estructura de directorios antes de ejecutar
    crear_estructura_directorios()
    
    # Ejecutar menú principal
    main()

