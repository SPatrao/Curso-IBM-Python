# book.py

class Book:
    """
    Clase para trabajar con libros.

    Atributos:
        title (str): Título del libro.
        author (str): Autor del libro.
        electronic (bool): Indica si el libro es electrónico.

    Métodos:
        __init__(self, title, author="", electronic=False): Constructor de la clase.
        __del__(self): Destructor de la clase.
    """
    def __init__(self, title, author="", electronic=False):
        self.title = title
        self.author = author
        self.is_electronic = electronic

    def __del__(self):
        print("Acabas de llamar al método destructor. El objeto acaba de ser eliminado.")


if __name__ == "__main__":
    # Ejemplo de uso
    book = Book("Lazarillo de Tormes", "Anónimo", True)
    print(f"Libro: {book.title}, Autor: {book.author}, Electrónico: {book.is_electronic}")
    del book