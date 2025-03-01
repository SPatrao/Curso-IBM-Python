class Libro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    @staticmethod
    def agregar():
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        while True:
            isbn = input("ISBN: ").strip()
            if isbn:
                break
            print("Error: El ISBN no puede estar vacío.")
        return Libro(titulo, autor, isbn)

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'Libro "{self.titulo}" prestado con éxito.')
        else:
            print(f'El libro "{self.titulo}" ya está prestado.')

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f'Libro "{self.titulo}" devuelto con éxito.')
        else:
            print(f'El libro "{self.titulo}" ya estaba disponible.')

    def mostrar(self):
        estado = "Sí" if self.disponible else "No"
        return f'- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}'

    def buscar(self):
        estado = "Sí" if self.disponible else "No"
        return f'{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}'

libros = []

def main():
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
            nuevo_libro = Libro.agregar()
            libros.append(nuevo_libro)
            print(f'Libro "{nuevo_libro.titulo}" agregado con éxito.')
        
        elif opcion == '2':
            isbn = input("ISBN del libro a prestar: ")
            libro = next((l for l in libros if l.isbn == isbn), None)
            if libro:
                libro.prestar()
            else:
                print("Libro no encontrado.")
        
        elif opcion == '3':
            isbn = input("ISBN del libro a devolver: ")
            libro = next((l for l in libros if l.isbn == isbn), None)
            if libro:
                libro.devolver()
            else:
                print("Libro no encontrado.")
        
        elif opcion == '4':
            if not libros:
                print("No hay libros en la biblioteca.")
            else:
                for libro in libros:
                    print(libro.mostrar())
        
        elif opcion == '5':
            isbn = input("ISBN del libro a buscar: ")
            libro = next((l for l in libros if l.isbn == isbn), None)
            if libro:
                print(libro.buscar())
            else:
                print("Libro no encontrado.")
        
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()  