import os

# Definimos la estructura del proyecto
estructura = {
    "PythonEstudio": {
        "01_introduccion": ["01_variables.py", "02_tipos_datos.py", "03_expresiones_regulares.py"],
        "02_control_flujo": ["01_condicionales.py", "02_bucles.py"],
        "03_excepciones": ["01_manejo_excepciones.py", "02_excepciones_personalizadas.py"],
        "04_funciones": ["01_definicion.py", "02_argumentos.py", "03_lambda.py", "04_funciones_avanzadas.py"],
        "05_estructuras_datos": ["01_listas.py", "02_tuplas.py", "03_diccionarios.py", "04_sets.py"],
        "06_modulos": ["01_modulos_nativos.py", "02_modulos_propios.py"],
        "07_manejo_archivos": ["01_csv_handler.py", "02_json_handler.py", "03_lectura_escritura.py"],
        "08_testing": ["01_testing_basico.py", "02_unittest.py", "03_pytest.py"],
        "09_numpy_y_pandas": ["01_intro_numpy.py", "02_intro_pandas.py"],
        "10_web_scraping": ["01_intro_beautifulsoup.py", "02_scraping_basico.py"],
        "11_aplicaciones_graficas": ["01_intro_tkinter.py", "02_aplicaciones_basicas.py"],
        "recursos.py": [],
        "glosario.py": [],
    }
}

# Creamos la estructura
for carpeta, archivos in estructura["PythonEstudio"].items():
    os.makedirs(os.path.join("PythonEstudio", carpeta), exist_ok=True)
    for archivo in archivos:
        open(os.path.join("PythonEstudio", carpeta, archivo), 'w').close()

print("Estructura de carpetas y archivos creada con éxito.")

