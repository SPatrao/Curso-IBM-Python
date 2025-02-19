# Importación de módulos necesarios
import os  # Para operaciones relacionadas con el sistema operativo
import venv  # Para crear entornos virtuales
import subprocess  # Para ejecutar comandos del sistema
import sys  # Para acceder a variables y funciones específicas del sistema

# Función para crear la estructura de directorios del proyecto
def create_directory_structure():
    """
    Esta función crea la estructura de directorios básica para el proyecto.
    Crea las carpetas 'data', 'src', 'notebooks' y 'tests'.
    También crea archivos vacíos: '__init__.py' en 'src' y 'README.md' en la raíz.
    """
    # Lista de directorios a crear
    directories = ['data', 'src', 'notebooks', 'tests']
    
    # Itera sobre la lista de directorios y los crea
    for directory in directories:
        # os.makedirs crea directorios recursivamente si no existen
        # exist_ok=True evita errores si el directorio ya existe
        os.makedirs(directory, exist_ok=True)
    
    # Crea archivos vacíos
    open('src/__init__.py', 'a').close()  # Crea __init__.py en src
    open('README.md', 'a').close()  # Crea README.md en la raíz

# Función para crear un entorno virtual

def create_virtual_environment():
    """
    Esta función crea un entorno virtual llamado 'venv' en el directorio actual.
    Utiliza el módulo venv de Python para crear el entorno.
    """
    # venv.create crea un nuevo entorno virtual
    # 'venv' es el nombre del directorio para el entorno virtual
    # with_pip=True asegura que pip esté instalado en el entorno virtual
    venv.create('venv', with_pip=True)

# Función para obtener el comando de activación del entorno virtual
def activate_virtual_environment():
    """
    Esta función determina el comando correcto para activar el entorno virtual
    basándose en el sistema operativo actual.
    Retorna el comando de activación como una cadena.
    """
    # Comprueba si el sistema operativo es Windows
    if sys.platform == 'win32':
        # En Windows, el script de activación está en una ubicación diferente
        activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
        # El comando para Windows usa 'call'
        activate_command = f'call {activate_script}'
    else:
        # Para sistemas Unix (Linux, macOS)
        activate_script = os.path.join('venv', 'bin', 'activate')
        # El comando para Unix usa 'source'
        activate_command = f'source {activate_script}'
    
    return activate_command

# Función para instalar las dependencias del proyecto
def install_dependencies():
    """
    Esta función crea un archivo requirements.txt con las dependencias del proyecto
    y luego las instala usando pip.
    """
    # Lista de paquetes a instalar
    requirements = [
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'jupyter'
    ]
    
    # Crea el archivo requirements.txt y escribe los paquetes
    with open('requirements.txt', 'w') as f:
        for req in requirements:
            f.write(f'{req}\n')
    
    # Instala los paquetes usando pip
    # sys.executable asegura que se use el Python del entorno virtual
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

# Función para configurar Git
def setup_git():
    """
    Esta función inicializa un repositorio Git y crea un archivo .gitignore.
    """
    # Inicializa un repositorio Git
    subprocess.check_call(['git', 'init'])
    
    # Contenido para el archivo .gitignore
    gitignore_content = '''
    venv/
    __pycache__/
    .ipynb_checkpoints/
    '''
    
    # Crea el archivo .gitignore y escribe el contenido
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)

# Función para crear un notebook inicial
def create_initial_notebook():
    """
    Esta función crea un notebook Jupyter inicial en la carpeta 'notebooks'.
    """
    # Contenido mínimo para un notebook Jupyter válido
    notebook_content = '''{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}'''
    
    # Crea el archivo del notebook y escribe el contenido
    with open('notebooks/01_data_exploration.ipynb', 'w') as f:
        f.write(notebook_content)

# Función principal que orquesta todo el proceso de configuración
def main():
    """
    Función principal que ejecuta todas las funciones de configuración
    en el orden correcto.
    """
    create_directory_structure()
    create_virtual_environment()
    activate_command = activate_virtual_environment()
    install_dependencies()
    setup_git()
    create_initial_notebook()
    
    print("Proyecto configurado exitosamente.")
    print(f"Para activar el entorno virtual, ejecuta: {activate_command}")

# Bloque de ejecución principal
if __name__ == '__main__':
    main()

