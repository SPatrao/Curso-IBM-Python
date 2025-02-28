class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro
        self.isbn = isbn  # Código ISBN del libro
        self.disponible = True  # Estado de disponibilidad (True = disponible, False = prestado)

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
        print(f'- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}')

    def buscar(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f'{self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Estado: {estado}')

# Lista para almacenar los libros
biblioteca = []

def agregar_libro():
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    while True:
        isbn = input("ISBN (mínimo 4 dígitos): ").strip()
        if len(isbn) >= 4 and isbn.isdigit():
            break
        print("Error: El ISBN debe contener al menos 4 dígitos numéricos.")
    
    nuevo_libro = Libro(titulo, autor, isbn)
    biblioteca.append(nuevo_libro)
    print(f'Libro "{titulo}" agregado con éxito.')

def prestar_libro():
    isbn = input("ISBN del libro a prestar: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.prestar()
            return
    print("Error: No se encontró un libro con ese ISBN.")

def devolver_libro():
    isbn = input("ISBN del libro a devolver: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.devolver()
            return
    print("Error: No se encontró un libro con ese ISBN.")

def mostrar_libros():
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    print("\nListado de libros en la biblioteca:")
    print("-" * 75)
    print(f"{'N°':<4}{'Título':<30}{'Autor':<20}{'ISBN':<15}{'Disponible'}")
    print("-" * 75)
    for i, libro in enumerate(biblioteca, 1):
        estado = "Sí" if libro.disponible else "No"
        print(f"{i:<4}{libro.titulo[:28]:<30}{libro.autor[:18]:<20}{libro.isbn:<15}{estado}")

def buscar_libro():
    isbn = input("ISBN del libro a buscar: ")
    for libro in biblioteca:
        if libro.isbn == isbn:
            libro.buscar()
            return
    print("Libro no encontrado.")

# Menú interactivo
if __name__ == "__main__":
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
            agregar_libro()
        elif opcion == '2':
            prestar_libro()
        elif opcion == '3':
            devolver_libro()
        elif opcion == '4':
            mostrar_libros()
        elif opcion == '5':
            buscar_libro()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
