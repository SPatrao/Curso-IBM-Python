class Libro:
    """
    Representa un libro en el sistema de gestión de la biblioteca.
    Esta clase define los atributos y comportamientos de un libro.
    """

    def __init__(self, titulo, autor, isbn):
        """
        Constructor de la clase Libro. Se llama automáticamente cuando se crea un nuevo objeto Libro.

        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            isbn (str): ISBN del libro (identificador único).
        """
        self.titulo = titulo  # Asigna el título del libro al atributo 'titulo' del objeto.
        self.autor = autor  # Asigna el autor del libro al atributo 'autor' del objeto.
        self.isbn = isbn  # Asigna el ISBN del libro al atributo 'isbn' del objeto.
        self.disponible = True  # Inicialmente, todos los libros están disponibles (True).

    @staticmethod
    def agregar(biblioteca, nuevo_libro):
        """
        Agrega un libro a la biblioteca. Este método es estático, lo que significa que se puede llamar
        directamente desde la clase (Libro.agregar()) sin necesidad de crear un objeto Libro.

        Args:
            biblioteca (list): La lista que representa la biblioteca a la que se va a añadir el libro.
            nuevo_libro (Libro): El objeto Libro que se va a añadir a la biblioteca.
        """
        biblioteca.append(nuevo_libro)  # Añade el nuevo libro a la lista de la biblioteca.
        print(f'Libro "{nuevo_libro.titulo}" agregado con éxito.')  # Muestra un mensaje de éxito.

    def prestar(self):
        """
        Marca el libro como prestado si está disponible.
        """
        if self.disponible:  # Comprueba si el libro está disponible.
            self.disponible = False  # Lo marca como no disponible (prestado).
            print(f'Libro "{self.titulo}" prestado con éxito.')  # Muestra mensaje de éxito.
        else:
            print(f'El libro "{self.titulo}" ya está prestado.')  # Muestra mensaje de que ya está prestado.

    def devolver(self):
        """
        Marca el libro como devuelto si estaba prestado.
        """
        if not self.disponible:  # Comprueba si el libro NO está disponible (está prestado).
            self.disponible = True  # Lo marca como disponible (devuelto).
            print(f'Libro "{self.titulo}" devuelto con éxito.')  # Muestra mensaje de éxito.
        else:
            print(f'El libro "{self.titulo}" ya estaba disponible.')  # Muestra mensaje de que ya estaba disponible.

    def mostrar(self):
        """
        Devuelve una cadena de texto con la información del libro (título, autor, ISBN y disponibilidad).

        Returns:
            str: Información del libro formateada como una cadena de texto.
        """
        estado = "Sí" if self.disponible else "No"  # Determina si se muestra "Sí" o "No" según la disponibilidad.
        return f'- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}'  # Devuelve la cadena formateada.

    def buscar(self):
        """
        Devuelve una cadena de texto con la información del libro (título, autor, ISBN y disponibilidad).

        Returns:
            str: Información del libro formateada como una cadena de texto.
        """
        estado = "Sí" if self.disponible else "No"  # Determina si se muestra "Sí" o "No" según la disponibilidad.
        return f'{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}'  # Devuelve la cadena formateada.

# Definición de excepciones personalizadas
class LibroNoEncontradoError(Exception):
    """Excepción para cuando no se encuentra un libro."""
    pass

class DatosInvalidosError(Exception):
    """Excepción para cuando los datos del libro son inválidos."""
    pass

class ISBNInvalidoError(Exception):
    """Excepción para cuando el ISBN es invalido."""
    pass

# Lista de libros (fuera de la clase)
biblioteca = []


def agregar_libro():
    """
    Función para agregar un nuevo libro a la biblioteca.
    Pide al usuario los detalles del libro y lo añade a la lista 'biblioteca'.
    """
    titulo = input("Título: ").strip()  # Pide el título y elimina espacios al principio/final.
    autor = input("Autor: ").strip()  # Pide el autor y elimina espacios al principio/final.
    
    if not titulo or not autor: # Validacion titulo y autor
        raise DatosInvalidosError("El título y el autor no pueden estar vacíos.")

    while True:
        isbn = input("ISBN (mínimo 4 dígitos): ").strip()  # Pide el ISBN y elimina espacios al principio/final.
        if len(isbn) >= 4 and isbn.isdigit():  # Comprueba que tenga al menos 4 dígitos y sean números.
            # Validación de ISBN repetido
            if any(libro.isbn == isbn for libro in biblioteca):
                raise ISBNInvalidoError(f"El ISBN '{isbn}' ya existe en la biblioteca.")
            break  # Sale del bucle si el ISBN es válido y no está repetido.
        raise ISBNInvalidoError(f"Error: El ISBN '{isbn}' debe contener al menos 4 dígitos numéricos.")

    nuevo_libro = Libro(titulo, autor, isbn)  # Crea un nuevo objeto Libro.
    Libro.agregar(biblioteca, nuevo_libro)  # Añade el nuevo libro a la lista de la biblioteca.


def prestar_libro():
    """
    Permite prestar un libro de la biblioteca.
    Pide al usuario el ISBN del libro que quiere prestar y llama al método prestar del libro encontrado.
    """
    isbn = input("ISBN del libro a prestar: ")  # Pide el ISBN del libro a prestar.
    for libro in biblioteca:  # Recorre la lista de libros en la biblioteca.
        if libro.isbn == isbn:  # Si el ISBN coincide con el de un libro.
            libro.prestar()  # Llama al método 'prestar' del libro encontrado.
            return  # Sale de la función.
    raise LibroNoEncontradoError(f"No se encontró un libro con el ISBN: {isbn}")  # Si no se encuentra el libro, lanza excepción.


def devolver_libro():
    """
    Permite devolver un libro a la biblioteca.
    Pide al usuario el ISBN del libro que quiere devolver y llama al método devolver del libro encontrado.
    """
    isbn = input("ISBN del libro a devolver: ")  # Pide el ISBN del libro a devolver.
    for libro in biblioteca:  # Recorre la lista de libros en la biblioteca.
        if libro.isbn == isbn:  # Si el ISBN coincide con el de un libro.
            libro.devolver()  # Llama al método 'devolver' del libro encontrado.
            return  # Sale de la función.
    raise LibroNoEncontradoError(f"No se encontró un libro con el ISBN: {isbn}")  # Si no se encuentra el libro, lanza excepción.


def mostrar_libros():
    """
    Muestra todos los libros en la biblioteca.
    """
    if not biblioteca:  # Comprueba si la biblioteca está vacía.
        print("La biblioteca está vacía.")  # Si está vacía, muestra un mensaje.
        return  # Sale de la función.
    print("\nListado de libros en la biblioteca:")
    print("-" * 75)  # Imprime una línea separadora.
    print(f"{'N°':<4}{'Título':<30}{'Autor':<20}{'ISBN':<15}{'Disponible'}")  # Imprime el encabezado de la tabla.
    print("-" * 75)  # Imprime una línea separadora.
    for i, libro in enumerate(biblioteca, 1):  # Recorre la lista de libros, 'i' es el número del libro.
        print(f"{i:<4}{libro.mostrar()}")  # Llama al método 'mostrar' del libro para imprimir su información.


def buscar_libro():
    """
    Busca un libro por ISBN y muestra sus datos.
    """
    isbn = input("ISBN del libro a buscar: ")  # Pide el ISBN del libro a buscar.
    for libro in biblioteca:  # Recorre la lista de libros en la biblioteca.
        if libro.isbn == isbn:  # Si el ISBN coincide con el de un libro.
            print(libro.buscar())  # Llama al método 'buscar' del libro encontrado para imprimir su información.
            return  # Sale de la función.
    raise LibroNoEncontradoError(f"No se encontró un libro con el ISBN: {isbn}")  # Si no se encuentra el libro, lanza excepción.

def main():
    """
    Función principal que ejecuta el menú interactivo.
    """
    while True:  # Bucle infinito hasta que el usuario decida salir.
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")

        opcion = input("Elige una opción: ")  # Pide al usuario que elija una opción.
        try:
            if opcion == '1':
                agregar_libro()  # Llama a la función para agregar un libro.
            elif opcion == '2':
                prestar_libro()  # Llama a la función para prestar un libro.
            elif opcion == '3':
                devolver_libro()  # Llama a la función para devolver un libro.
            elif opcion == '4':
                mostrar_libros()  # Llama a la función para mostrar los libros.
            elif opcion == '5':
                buscar_libro()  # Llama a la función para buscar un libro.
            elif opcion == '6':
                print("Saliendo del sistema...")  # Mensaje de despedida.
                break  # Sale del bucle y termina el programa.
            else:
                 raise ValueError("Opción de menú inválida.")  # Si la opción no es válida, lanza excepcion.
        except LibroNoEncontradoError as e:
            print(e)
        except DatosInvalidosError as e:
            print(e)
        except ValueError as e:
            print(e)
        except ISBNInvalidoError as e:
            print(e)
if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa.

