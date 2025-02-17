import os  # Proporciona una forma de interactuar con el sistema operativo, como la gestión de archivos y directorios.
import importlib  # Utilizado para importar módulos de forma dinámica en tiempo de ejecución.
import importlib.util  # Herramientas auxiliares para gestionar la importación dinámica de módulos.

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from datetime import datetime  # Importar la clase datetime
from usuarios import PROGRESO_USUARIOS
# Diccionario de rutas de módulos actualizado
# Cada categoría (clave) tiene una lista de archivos (valores) que representan los módulos disponibles.
import subprocess  # Importamos la función subprocess
import sys  # Importa el módulo sys

try:
    import reportlab
except ImportError:
    print("La biblioteca 'reportlab' no está instalada. Procediendo a instalarla...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
        print("Biblioteca 'reportlab' instalada correctamente.")
    except subprocess.CalledProcessError as e:
        print("Error al instalar la biblioteca 'reportlab':", e)
        exit(1)

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
    """Función para limpiar la pantalla dependiendo del sistema operativo.
    En sistemas Windows (nt) ejecuta 'cls' y en otros sistemas ejecuta 'clear'."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Ejecuta el comando adecuado para limpiar la pantalla.

def generar_certificado_final(usuario):
    """Genera un certificado final en formato PDF para el usuario."""
    try:
        ruta_certificado = get_ruta_archivo(f"certificado_final_{usuario}.pdf")
        print(f"Ruta del certificado final: {ruta_certificado}")
        
        # Crear el documento PDF
        doc = SimpleDocTemplate(ruta_certificado, pagesize=letter)
        elements = []

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Centered', alignment=1))

        elements.append(Paragraph(f"CERTIFICADO DE FINALIZACIÓN", styles["Centered"]))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Se otorga este certificado a", styles["BodyText"]))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"{usuario}", styles["Heading1"]))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"por haber completado satisfactoriamente el", styles["BodyText"]))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"CURSO DE PYTHON", styles["Heading1"]))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(f"Expedido el {datetime.now().strftime('%d de %B de %Y')}", styles["BodyText"]))

        doc.build(elements)
        os.system(f"open {ruta_certificado}")  # Abrimos el certificado en el visor de PDF
    except Exception as error:
        print("Error al generar certificado final:", error)

def get_ruta_archivo(nombre_archivo):
    """Obtiene la ruta completa de un archivo dentro del directorio del proyecto."""
    proyecto_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(proyecto_dir, nombre_archivo)

def mostrar_progreso(usuario):
    """Muestra el progreso del usuario en el curso."""
    limpiar_pantalla()
    print(f"=== PROGRESO DE {usuario.upper()} ===")

    for categoria in MODULOS:
        estado = "Completado" if PROGRESO_USUARIOS[usuario].get(categoria, False) else "Incompleto"
        print(f"{categoria}: {estado}")

    input("\nPresione Enter para continuar...")

def mostrar_menu_principal(usuario):
    """Muestra el menú principal con las categorías de módulos disponibles.
    Permite al usuario seleccionar una categoría para ver los módulos dentro de ella."""
    limpiar_pantalla()
    print("=== MENÚ PRINCIPAL DE PYTHON ===")
    print(f"Usuario: {usuario}")
    print("Seleccione una opción:")
    print("1. Ver módulos")
    print("2. Ver mi progreso")
    print("3. Seleccionar categoría")
    print("0. Salir")

    return input("Opción: ")

def mostrar_modulos(usuario, categoria):
    """Muestra los módulos de una categoría seleccionada.
    Permite al usuario elegir un módulo dentro de la categoría especificada."""
    limpiar_pantalla()
    
    # Verificar si el usuario tiene un registro en PROGRESO_USUARIOS
    if usuario not in PROGRESO_USUARIOS or categoria not in PROGRESO_USUARIOS[usuario]:
        print(f"El usuario {usuario} no tiene registros para la categoría {categoria}.")
        input("Presione Enter para continuar...")
        return "0"
    
    modulos = MODULOS[categoria]
    print(f"=== MÓDULOS DE {categoria.upper()} ===")

    for i, modulo in enumerate(modulos, 1):
        print(f"{i}. {modulo}")
    print("0. Volver al menú principal")

    return input("Seleccione un módulo: ")

def registrar_completitud(usuario, modulo):
    """Registra la completitud de un módulo por parte del usuario."""
    try:
        ruta_registros = get_ruta_archivo("registros.txt")
        with open(ruta_registros, "a") as archivo_registro:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo_registro.write(f"{fecha_hora} - Usuario {usuario} ha completado el módulo {modulo}\n")
    except Exception as error:
        print("Error al registrar el progreso del usuario:", error)

def generar_certificado(usuario, categoria):
    """Genera un certificado de finalización para el usuario en una categoría."""
    try:
        ruta_certificados = get_ruta_archivo("certificados")
        if not os.path.exists(ruta_certificados):
            os.makedirs(ruta_certificados)

        # Verificamos si el usuario ha completado todos los módulos de la categoría
        if all(PROGRESO_USUARIOS[usuario].get(categoria, False)):
            certificado_file = os.path.join(ruta_certificados, f"certificado_{categoria}_{usuario}.txt")
            with open(certificado_file, "w") as archivo_certificado:
                fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo_certificado.write(f"{fecha_hora} - Usuario {usuario}, ha completado todos los módulos de la categoría {categoria}.")
            os.system(f"open {certificado_file}")  # Abrimos el archivo en el navegador
        else:
            print(f"El usuario {usuario} aún no ha completado todos los módulos de la categoría {categoria}.")
    except Exception as error:
        print("Error al generar certificado:", error)

def cargar_progreso_usuarios():
    """Carga el progreso de los usuarios desde el archivo usuarios.py."""
    ruta_archivo = get_ruta_archivo("usuarios.py")
    try:
        with open(ruta_archivo, "r") as archivo:
            exec(archivo.read())
        return PROGRESO_USUARIOS
    except (FileNotFoundError, NameError):
        # Si el archivo usuarios.py no existe o PROGRESO_USUARIOS no está definido, crear uno nuevo
        with open(ruta_archivo, "w") as archivo:
            archivo.write("PROGRESO_USUARIOS = {}")
        return {}

def actualizar_progreso(usuario, categoria, modulo, progreso_usuarios):
    """Actualiza el progreso del usuario en una categoría."""
    progreso_usuarios[usuario][categoria] = all(
        modulo in MODULOS[categoria] for modulo in MODULOS[categoria]
    )

    if all(progreso_usuarios[usuario].values()):
        generar_certificado(usuario, categoria)
        generar_certificado_final(usuario)

    # Guardar el progreso de los usuarios en usuarios.py
    usuarios_py = get_ruta_archivo("usuarios.py")
    with open(usuarios_py, "w") as archivo:
        archivo.write(f"PROGRESO_USUARIOS = {repr(progreso_usuarios)}")

def ejecutar_modulo(categoria, modulo, usuario, progreso_usuarios):
    """Ejecuta un módulo seleccionado de una categoría específica.
    Importa dinámicamente el módulo, lo ejecuta y registra la completitud."""
    try:
        limpiar_pantalla()
        ruta_completa = os.path.join(os.getcwd(), "curso_python", categoria, modulo)

        if not os.path.exists(ruta_completa):
            print(f"Error: El archivo {modulo} no existe en {categoria}")
            input("Presione Enter para continuar...")
            return

        spec = importlib.util.spec_from_file_location(modulo, ruta_completa)
        modulo_importado = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo_importado)

        registrar_completitud(usuario, modulo)
        actualizar_progreso(usuario, categoria, modulo, progreso_usuarios)

        if all(progreso_usuarios[usuario].values()):
            generar_certificado(usuario, categoria)

        print(f"¡Felicidades, has completado el módulo {modulo}!")
        input("\nPresione Enter para continuar...")
    except Exception as e:
        print(f"Error al ejecutar el módulo {modulo}: {e}")
        input("\nPresione Enter para continuar...")

def mostrar_seleccionar_categoria(usuario):
    """Muestra las categorías disponibles y permite al usuario seleccionar una."""
    limpiar_pantalla()
    print("=== SELECCIONAR CATEGORÍA ===")
    print(f"Usuario: {usuario}")
    print("Seleccione una categoría:")

    categorias_disponibles = []
    for i, categoria in enumerate(MODULOS.keys(), 1):
        if categoria in PROGRESO_USUARIOS[usuario]:
            categorias_disponibles.append(categoria)
            print(f"{i}. {categoria}")

    if not categorias_disponibles:
        print("No tienes registros de progreso en ninguna categoría.")
        input("Presione Enter para continuar...")
        return "0"

    print("0. Volver al menú principal")
    return input("Opción: ")

def crear_estructura_directorios():
    """Crea los directorios correspondientes si no existen.
    Crea un directorio por cada categoría para organizar los módulos."""
    proyecto_dir = get_ruta_archivo("")
    directorios = list(MODULOS.keys())
    for directorio in directorios:
        directorio_completo = os.path.join(proyecto_dir, directorio)
        if not os.path.exists(directorio_completo):
            os.makedirs(directorio_completo)
            print(f"Creado directorio: {directorio_completo}")

def main():
    """Función principal que gestiona el flujo de ejecución del menú."""
    # Cargar el progreso de los usuarios desde usuarios.py
    PROGRESO_USUARIOS = cargar_progreso_usuarios()

    # Solicita el nombre del usuario al comenzar el programa
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario not in PROGRESO_USUARIOS:
        PROGRESO_USUARIOS[usuario] = {
            '01_introduccion': False,
            '02_estructuras_control': False,
            '03_funciones': False,
            '04_estructura_datos': False,
            '05_poo': False,
            '06_modulos': False,
            '07_manejo_archivos': False,
            '08_excepciones_personalizadas': False,
            '09_decoradores': False,
            '10_generadores': False,
            '11_programacion_funcional': False,
        }

    while True:
        opcion = mostrar_menu_principal(usuario)

        if opcion == '0':
            break
        elif opcion == '1':
            categoria_seleccionada = None
            while True:
                if categoria_seleccionada is None:
                    opcion_categoria = mostrar_seleccionar_categoria(usuario)
                    if opcion_categoria == '0':
                        break
                    categoria_seleccionada = list(MODULOS.keys())[int(opcion_categoria) - 1]
                opcion_modulo = mostrar_modulos(usuario, categoria_seleccionada)
                if opcion_modulo == '0':
                    categoria_seleccionada = None
                    break
                try:
                    modulo_seleccionado = MODULOS[categoria_seleccionada][int(opcion_modulo) - 1]
                    ejecutar_modulo(categoria_seleccionada, modulo_seleccionado, usuario, PROGRESO_USUARIOS)
                except (ValueError, IndexError):
                    print("Opción de módulo inválida")
                    input("Presione Enter para continuar...")
        elif opcion == '2':
            mostrar_progreso(usuario)
        elif opcion == '3':
            opcion_categoria = mostrar_seleccionar_categoria(usuario)
            if opcion_categoria != '0':
                categoria_seleccionada = list(MODULOS.keys())[int(opcion_categoria) - 1]
            else:
                categoria_seleccionada = None
        else:
            print("Opción inválida")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    crear_estructura_directorios()
    main()