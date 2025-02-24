import csv

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo  
        self.autor = autor  
        self.isbn = isbn  
        self.disponible = True  

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'Libro "{self.titulo}" prestado con éxito.')
            return True
        else:
            print(f'El libro "{self.titulo}" ya está prestado.')
            return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f'Libro "{self.titulo}" devuelto con éxito.')
            return True
        else:
            print(f'El libro "{self.titulo}" ya estaba disponible.')
            return False

    def mostrar(self):
        estado = 'Sí' if self.disponible else 'No'
        return f'- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}'
    
    def buscar(self):
        estado = 'Disponible' if self.disponible else 'No disponible'
        return f'{self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Estado: {estado}'

    def agregar(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        print(f'Libro "{self.titulo}" agregado con éxito (ISBN: {self.isbn}).')

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.isbn_counter = 100000000  

    def generar_isbn_continuo(self):
        while str(self.isbn_counter) in self.libros:
            self.isbn_counter += 1  
        return str(self.isbn_counter)

    def validar_isbn(self, isbn):
        return isbn.isdigit() and len(isbn) == 10

    def agregar_libro(self, titulo, autor, isbn=None):
        if not isbn:
            isbn = self.generar_isbn_continuo()
            print(f"ISBN generado automáticamente: {isbn}")

        elif not self.validar_isbn(isbn):
            print("El ISBN debe ser un número de 10 dígitos.")
            return

        if isbn in self.libros:
            print(f"El libro con ISBN {isbn} ya está en la biblioteca.")
            return

        libro = Libro(titulo, autor, isbn)
        self.libros[isbn] = libro
        print(f'Libro "{titulo}" agregado con éxito (ISBN: {isbn}).')

    def prestar_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            libro.prestar()
        else:
            print(f"Error: No se encontró un libro con ISBN {isbn}.")

    def devolver_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            libro.devolver()
        else:
            print(f"Error: No se encontró un libro con ISBN {isbn}.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
            return
        
        print("\nListado de libros en la biblioteca:")
        print("-" * 75)
        print(f"{'N°':<4}{'Título':<30}{'Autor':<20}{'ISBN':<15}{'Disponible'}")
        print("-" * 75)

        for i, libro in enumerate(self.libros.values(), 1):
            estado = "Sí" if libro.disponible else "No"
            print(f"{i:<4}{libro.titulo[:28]:<30}{libro.autor[:18]:<20}{libro.isbn:<15}{estado}")

    def cargar_libros_csv(self, archivo_csv):
        try:
            with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.DictReader(archivo)
                
                for fila in lector_csv:
                    titulo = fila.get('Title', '').strip()
                    autor = fila.get('Author', 'Desconocido').strip()
                    if titulo:
                        self.agregar_libro(titulo, autor)

            print("Carga de libros completada.")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo_csv}.")
        except Exception as e:
            print(f"Error al cargar el archivo CSV: {e}")

# Interfaz de usuario
if __name__ == "__main__":
    biblioteca = Biblioteca()
    
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Cargar libros desde CSV")
        print("7. Salir")

        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN (Dejar en blanco para generar automáticamente): ")
            if not isbn:
                biblioteca.agregar_libro(titulo, autor)
            else:
                biblioteca.agregar_libro(titulo, autor, isbn)

        elif opcion == '2':
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(isbn)

        elif opcion == '3':
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)

        elif opcion == '4':
            biblioteca.mostrar_libros()

        elif opcion == '5':
            isbn = input("ISBN del libro a buscar: ")
            libro = biblioteca.libros.get(isbn)
            if libro:
                print(libro.buscar())
            else:
                print("Libro no encontrado.")

        elif opcion == '6':
            biblioteca.cargar_libros_csv("skyrim_books.csv")

        elif opcion == '7':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
