# MANEJO DE ARCHIVOS CSV
# Importación de las bibliotecas necesarias para trabajar con archivos CSV.
import csv  # Biblioteca estándar para trabajar con archivos CSV
import pandas as pd  # Biblioteca externa para manejo de datos tabulares, muy útil para CSV y otros formatos

# Función para escribir datos en un archivo CSV
def escribir_csv():
    """
    Esta función escribe un conjunto de datos en un archivo CSV llamado 'usuarios.csv'.
    Los datos son definidos como una lista de listas. Cada sublista representa una fila
    en el archivo CSV.
    """
    # Definición de los datos que se escribirán en el archivo CSV.
    # La primera lista contiene los encabezados de las columnas (campos del CSV).
    # Las siguientes listas contienen los datos correspondientes a cada fila.
    datos = [
        ['Nombre', 'Edad', 'Ciudad'],  # Encabezados
        ['Juan', 30, 'Madrid'],        # Fila 1
        ['María', 25, 'Barcelona'],    # Fila 2
        ['Pedro', 35, 'Valencia']      # Fila 3
    ]
    
    # Usamos 'open' para abrir (o crear si no existe) el archivo 'usuarios.csv'.
    # Se especifica 'w' para escribir en el archivo. 'newline=""' previene saltos de línea extra en algunos sistemas.
    with open('usuarios.csv', 'w', newline='') as archivo:
        # 'csv.writer()' se usa para crear un objeto que escribe datos en el archivo CSV.
        escritor = csv.writer(archivo)
        
        # 'writerows()' escribe todas las filas de la lista 'datos' en el archivo.
        escritor.writerows(datos)

# Función para leer un archivo CSV usando el método tradicional de la biblioteca 'csv'
def leer_csv_tradicional():
    """
    Esta función lee los datos de un archivo CSV utilizando el método tradicional de la librería 'csv'.
    Lee línea por línea y las imprime por consola.
    """
    # Abrir el archivo 'usuarios.csv' en modo lectura ('r').
    with open('usuarios.csv', 'r') as archivo:
        # 'csv.reader()' se usa para leer el archivo CSV. El lector recorrerá cada fila del archivo.
        lector = csv.reader(archivo)
        
        # Iteramos sobre cada fila que el lector lee del archivo CSV.
        for fila in lector:
            # Imprimimos cada fila del archivo.
            print(fila)

# Función para leer un archivo CSV usando Pandas
def leer_csv_pandas():
    """
    Esta función lee un archivo CSV utilizando la biblioteca Pandas.
    Pandas carga los datos en un DataFrame, que es una estructura tabular más fácil de manipular.
    """
    # 'pd.read_csv()' lee el archivo CSV y lo convierte en un DataFrame de Pandas.
    # Los DataFrames permiten operaciones avanzadas como filtrado, agrupación y cálculo de estadísticas.
    df = pd.read_csv('usuarios.csv')
    
    # Imprimimos el DataFrame completo (todos los datos del CSV).
    print(df)
    
    # Realizamos algunas operaciones adicionales con Pandas:
    
    # Cálculo de la edad media usando la columna 'Edad'. 'mean()' calcula el promedio.
    print("\nEdad media:")
    print(df['Edad'].mean())  # Salida: Promedio de las edades
    
    # Filtrado de los datos para mostrar solo las filas donde la ciudad es 'Madrid'.
    print("\nFiltrar por ciudad:")
    print(df[df['Ciudad'] == 'Madrid'])  # Solo muestra las filas con 'Madrid' en la columna 'Ciudad'

# Bloque principal que se ejecuta si este archivo se ejecuta directamente.
if __name__ == "__main__":
    # Llamada a la función que escribe los datos en el archivo CSV.
    escribir_csv()
    
    # Llamada a la función que lee el archivo CSV usando el método tradicional.
    leer_csv_tradicional()
    
    # Llamada a la función que lee el archivo CSV usando Pandas y muestra estadísticas.
    leer_csv_pandas()
