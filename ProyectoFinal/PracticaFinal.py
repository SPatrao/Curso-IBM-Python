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

    def agregar():
        """Método estático para solicitar datos de un nuevo libro y validarlos."""
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        while True:
            isbn = input("ISBN (mínimo 4 dígitos): ").strip()
            if len(isbn) >= 4 and isbn.isdigit():
                break
            print("Error: El ISBN debe contener al menos 4 dígitos numéricos.")
        
        return Libro(titulo, autor, isbn)

class Biblioteca:
    def __init__(self):
        self.libros = {} 

    def agregar_libro(self):
        nuevo_libro = Libro.agregar()
        if nuevo_libro.isbn in self.libros:
            print(f"El libro con ISBN {nuevo_libro.isbn} ya está en la biblioteca.")
            return
        self.libros[nuevo_libro.isbn] = nuevo_libro
        print(f'Libro "{nuevo_libro.titulo}" agregado con éxito (ISBN: {nuevo_libro.isbn}).')

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
        print("6. Salir")

        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            biblioteca.agregar_libro()

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
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
