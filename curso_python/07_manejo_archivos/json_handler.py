# MANEJO DE ARCHIVOS JSON
import json

def escribir_json():
    """Escribir datos en formato JSON"""
    datos = {
        "nombre": "Juan Pérez",
        "edad": 30,
        "ciudad": "Madrid",
        "cursos": ["Python", "Data Science", "Machine Learning"]
    }
    
    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def leer_json():
    """Leer archivo JSON"""
    try:
        with open('datos.json', 'r') as archivo:
            datos = json.load(archivo)
            print("Datos leídos:")
            print(json.dumps(datos, indent=2))
    except FileNotFoundError:
        print("Archivo JSON no encontrado")

def modificar_json():
    """Modificar datos en JSON"""
    try:
        with open('datos.json', 'r+') as archivo:
            datos = json.load(archivo)
            datos['nuevo_campo'] = "Valor añadido"
            
            # Regresar al inicio del archivo
            archivo.seek(0)
            json.dump(datos, archivo, indent=4)
            archivo.truncate()  # Borrar contenido restante
    except FileNotFoundError:
        print("Archivo JSON no encontrado")

if __name__ == "__main__":
    escribir_json()
    leer_json()
    modificar_json()

