# MANEJO DE ARCHIVOS CSV
import csv
import pandas as pd

def escribir_csv():
    """Escribir datos en un archivo CSV"""
    datos = [
        ['Nombre', 'Edad', 'Ciudad'],
        ['Juan', 30, 'Madrid'],
        ['María', 25, 'Barcelona'],
        ['Pedro', 35, 'Valencia']
    ]
    
    with open('usuarios.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)

def leer_csv_tradicional():
    """Leer CSV con método tradicional"""
    with open('usuarios.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(fila)

def leer_csv_pandas():
    """Leer CSV con Pandas"""
    df = pd.read_csv('usuarios.csv')
    print(df)
    
    # Operaciones con Pandas
    print("\nEdad media:")
    print(df['Edad'].mean())
    
    print("\nFiltrar por ciudad:")
    print(df[df['Ciudad'] == 'Madrid'])

if __name__ == "__main__":
    escribir_csv()
    leer_csv_tradicional()
    leer_csv_pandas()

