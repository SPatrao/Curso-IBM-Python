import streamlit as st
import csv
import pandas as pd
from io import StringIO
import requests

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo  
        self.autor = autor  
        self.isbn = isbn  
        self.disponible = True  

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True, f'Libro "{self.titulo}" prestado con éxito.'
        else:
            return False, f'El libro "{self.titulo}" ya está prestado.'

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True, f'Libro "{self.titulo}" devuelto con éxito.'
        else:
            return False, f'El libro "{self.titulo}" ya estaba disponible.'

    def buscar(self):
        estado = 'Disponible' if self.disponible else 'No disponible'
        return f'{self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Estado: {estado}'

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.isbn_counter = 100000000  

    def generar_isbn_continuo(self):
        while str(self.isbn_counter) in self.libros:
            self.isbn_counter += 1  
        return str(self.isbn_counter)

    def validar_isbn(self, isbn):
        # Validamos que sea un número y permitimos de 9 a 10 dígitos (formatos comunes de ISBN)
        return isbn.isdigit() and (9 <= len(isbn) <= 10)

    def agregar_libro(self, titulo, autor, isbn=None):
        if not titulo or not autor:
            return False, "El título y el autor son obligatorios."
            
        if not isbn or isbn.strip() == "":
            isbn = self.generar_isbn_continuo()
            mensaje_isbn = f"ISBN generado automáticamente: {isbn}"
        elif not self.validar_isbn(isbn):
            return False, f"El ISBN debe ser un número de entre 9 y 10 dígitos. Recibido: '{isbn}' con {len(isbn)} dígitos."
        else:
            mensaje_isbn = ""

        if isbn in self.libros:
            return False, f"El libro con ISBN {isbn} ya está en la biblioteca."

        libro = Libro(titulo, autor, isbn)
        self.libros[isbn] = libro
        mensaje = f'Libro "{titulo}" agregado con éxito (ISBN: {isbn}).'
        if mensaje_isbn:
            mensaje = f"{mensaje} {mensaje_isbn}"
        return True, mensaje

    def prestar_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            return libro.prestar()
        else:
            return False, f"Error: No se encontró un libro con ISBN {isbn}."

    def devolver_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            return libro.devolver()
        else:
            return False, f"Error: No se encontró un libro con ISBN {isbn}."

    def buscar_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            return True, libro.buscar()
        else:
            return False, f"No se encontró un libro con ISBN {isbn}."

    def obtener_libros_dataframe(self):
        if not self.libros:
            return pd.DataFrame()
        
        datos = []
        for libro in self.libros.values():
            datos.append({
                'Título': libro.titulo,
                'Autor': libro.autor,
                'ISBN': libro.isbn,
                'Disponible': 'Sí' if libro.disponible else 'No'
            })
        
        return pd.DataFrame(datos)

    def cargar_libros_csv(self, contenido_csv):
        try:
            csv_io = StringIO(contenido_csv)
            lector_csv = csv.DictReader(csv_io)
            
            libros_agregados = 0
            for fila in lector_csv:
                titulo = fila.get('Title', '').strip()
                autor = fila.get('Author', 'Desconocido').strip()
                if titulo:
                    self.agregar_libro(titulo, autor)
                    libros_agregados += 1

            return True, f"Carga de libros completada. Se agregaron {libros_agregados} libros."
        except Exception as e:
            return False, f"Error al cargar el archivo CSV: {e}"

# Función para guardar el estado en session_state
def inicializar_biblioteca():
    if 'biblioteca' not in st.session_state:
        st.session_state.biblioteca = Biblioteca()
    return st.session_state.biblioteca

# Aplicación Streamlit
def main():

    st.set_page_config(
        page_title="Sistema de Gestión de Biblioteca",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("📚 Sistema de Gestión de Biblioteca")
    
    # Inicializar la biblioteca
    biblioteca = inicializar_biblioteca()
    # Cargar libros iniciales desde un archivo CSV
    url = 'https://raw.githubusercontent.com/RomanOsma/Curso-IBM-Python/main/ProyectoFinal/skyrim_books.csv'
    try:
        response = requests.get(url)
        response.raise_for_status()
        contenido_csv = response.text
        biblioteca.cargar_libros_csv(contenido_csv)
    except requests.exceptions.RequestException as e:
        st.warning(f"Error al cargar el archivo CSV desde la web: {e}")
    
    # Inicializar variables de estado si no existen
    if 'isbn_manual' not in st.session_state:
        st.session_state.isbn_manual = False
    
    # Menú lateral
    with st.sidebar:
        st.header("Menú")
        pagina = st.radio(
            "Selecciona una opción:",
            ["Inicio", "Agregar Libro", "Gestionar Préstamos", "Buscar Libro", "Importar CSV"]
        )
    
    # Página de inicio
    if pagina == "Inicio":
        st.header("Listado de Libros")
        df = biblioteca.obtener_libros_dataframe()
        
        if df.empty:
            st.info("La biblioteca está vacía. Comienza agregando libros.")
        else:
            # Filtros
            col1, col2 = st.columns(2)
            with col1:
                mostrar_disponibles = st.checkbox("Solo mostrar disponibles", value=False)
            with col2:
                buscar_titulo = st.text_input("Buscar por título:")
            
            # Aplicar filtros
            if mostrar_disponibles:
                df = df[df['Disponible'] == 'Sí']
            
            if buscar_titulo:
                df = df[df['Título'].str.contains(buscar_titulo, case=False)]
            
            # Mostrar tabla
            st.dataframe(df, use_container_width=True)
            
            st.write(f"Total de libros: {len(biblioteca.libros)}")
            st.write(f"Libros disponibles: {sum(1 for libro in biblioteca.libros.values() if libro.disponible)}")
    
    # Página para agregar libros
    elif pagina == "Agregar Libro":
        st.header("Agregar Nuevo Libro")
        
        with st.form("formulario_libro"):
            titulo = st.text_input("Título del libro:")
            autor = st.text_input("Autor:")
            
            # Checkbox para habilitar ISBN manual
            isbn_manual = st.checkbox("Ingresar ISBN manualmente", value=st.session_state.isbn_manual)
            st.session_state.isbn_manual = isbn_manual
            
            # Campo ISBN
            if isbn_manual:
                isbn = st.text_input("ISBN (9-10 dígitos):")
            else:
                st.text_input("ISBN (se generará automáticamente):", disabled=True)
                isbn = ""
            
            submitted = st.form_submit_button("Agregar Libro")
            
            if submitted:
                if isbn_manual and isbn:
                    exito, mensaje = biblioteca.agregar_libro(titulo, autor, isbn)
                else:
                    exito, mensaje = biblioteca.agregar_libro(titulo, autor)
                
                if exito:
                    st.success(mensaje)
                else:
                    st.error(mensaje)
    
    # Página para gestionar préstamos
    elif pagina == "Gestionar Préstamos":
        st.header("Gestión de Préstamos")
        
        tabs = st.tabs(["Prestar Libro", "Devolver Libro"])
        
        with tabs[0]:
            st.subheader("Prestar Libro")
            isbn_prestamo = st.text_input("ISBN del libro a prestar:", key="prestamo_isbn")
            if st.button("Prestar"):
                if isbn_prestamo:
                    exito, mensaje = biblioteca.prestar_libro(isbn_prestamo)
                    if exito:
                        st.success(mensaje)
                    else:
                        st.error(mensaje)
                else:
                    st.warning("Por favor, ingresa un ISBN.")
        
        with tabs[1]:
            st.subheader("Devolver Libro")
            isbn_devolucion = st.text_input("ISBN del libro a devolver:", key="devolucion_isbn")
            if st.button("Devolver"):
                if isbn_devolucion:
                    exito, mensaje = biblioteca.devolver_libro(isbn_devolucion)
                    if exito:
                        st.success(mensaje)
                    else:
                        st.error(mensaje)
                else:
                    st.warning("Por favor, ingresa un ISBN.")
    
    # Página para buscar libros
    elif pagina == "Buscar Libro":
        st.header("Buscar Libro")
        
        isbn_busqueda = st.text_input("Ingresa el ISBN del libro a buscar:")
        if st.button("Buscar"):
            if isbn_busqueda:
                exito, resultado = biblioteca.buscar_libro(isbn_busqueda)
                if exito:
                    st.success("Libro encontrado")
                    st.write(resultado)
                else:
                    st.error(resultado)
            else:
                st.warning("Por favor, ingresa un ISBN para buscar.")
    
    # Página para importar CSV
    elif pagina == "Importar CSV":
        st.header("Importar Libros desde CSV")
        
        st.write("Sube un archivo CSV con columnas 'Title' y 'Author'.")
        archivo_csv = st.file_uploader("Selecciona el archivo CSV", type=['csv'])
        
        if archivo_csv is not None:
            # Leer el contenido del archivo
            contenido = archivo_csv.getvalue().decode('utf-8')
            
            # Mostrar vista previa
            st.subheader("Vista previa del CSV")
            df_preview = pd.read_csv(StringIO(contenido))
            st.dataframe(df_preview.head(), use_container_width=True)
            
            if st.button("Importar Libros"):
                exito, mensaje = biblioteca.cargar_libros_csv(contenido)
                if exito:
                    st.success(mensaje)
                else:
                    st.error(mensaje)

if __name__ == "__main__":
    main()