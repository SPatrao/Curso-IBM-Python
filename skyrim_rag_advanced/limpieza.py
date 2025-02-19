import os
import shutil
import glob

def limpiar_proyecto():
    # Lista de patrones de archivos y carpetas a eliminar
    patrones = [
        '**/__pycache__',
        '**/*.pyc',
        '**/*.pyo',
        '**/*.pyd',
        '**/*.so',
        '**/.pytest_cache',
        '**/.mypy_cache',
        '**/.ipynb_checkpoints',
        '**/build',
        '**/dist',
        '**/*.egg-info',
        '**/.streamlit',
        # Agrega aquí más patrones si es necesario
    ]

    # Archivos específicos que quieres eliminar (si los hay)
    archivos_especificos = [
        # 'ruta/al/archivo.extension',
    ]

    contador = 0
    errores = 0

    # Obtener la ruta absoluta del entorno virtual
    venv_path = os.path.abspath('venv')

    # Función para verificar si una ruta está dentro del entorno virtual
    def es_parte_de_venv(ruta):
        return os.path.abspath(ruta).startswith(venv_path)

    # Eliminar archivos y carpetas que coinciden con los patrones
    for patron in patrones:
        for ruta in glob.glob(patron, recursive=True):
            if es_parte_de_venv(ruta):
                continue  # Saltar archivos/carpetas dentro del entorno virtual
            try:
                if os.path.isfile(ruta):
                    os.remove(ruta)
                elif os.path.isdir(ruta):
                    shutil.rmtree(ruta)
                print(f"Eliminado: {ruta}")
                contador += 1
            except PermissionError:
                print(f"Error de permisos: No se pudo eliminar {ruta}")
                errores += 1
            except Exception as e:
                print(f"Error al eliminar {ruta}: {e}")
                errores += 1

    # Eliminar archivos específicos
    for archivo in archivos_especificos:
        if os.path.exists(archivo) and not es_parte_de_venv(archivo):
            try:
                os.remove(archivo)
                print(f"Eliminado: {archivo}")
                contador += 1
            except PermissionError:
                print(f"Error de permisos: No se pudo eliminar {archivo}")
                errores += 1
            except Exception as e:
                print(f"Error al eliminar {archivo}: {e}")
                errores += 1

    print(f"Limpieza completada. Se eliminaron {contador} elementos.")
    if errores > 0:
        print(f"Se encontraron {errores} errores durante la limpieza.")

if __name__ == "__main__":
    limpiar_proyecto()

