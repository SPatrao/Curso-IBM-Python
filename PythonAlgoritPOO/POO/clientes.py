# clientes.py

class Cliente:
    """
    Esta clase representa a un cliente con atributos como DNI, nombre y apellidos.
    Tiene un método para mostrar la información del cliente.

    Atributos:
        dni (str): El DNI del cliente.
        nombre (str): El nombre del cliente.
        apellidos (str): Los apellidos del cliente.

    Métodos:
        __init__(self, dni, nombre, apellidos): Constructor de la clase.
        __str__(self): Retorna una representación en cadena del objeto Cliente.
    """
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Empresa:
    """
    Esta clase representa a una empresa con una lista de clientes.
    Tiene métodos para mostrar y borrar clientes de la lista.

    Atributos:
        clientes (list): Una lista de objetos Cliente.

    Métodos:
        __init__(self, clientes=None): Constructor de la clase.
        mostrar_cliente(self, dni): Muestra la información de un cliente por su DNI.
        borrar_cliente(self, dni): Borra un cliente de la lista por su DNI.
    """
    def __init__(self, clientes=None):
        self.clientes = clientes if clientes is not None else []

    def mostrar_cliente(self, dni):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni):
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del self.clientes[i]
                print(f"{c} > BORRADO")
                return
        print("Cliente no encontrado")


if __name__ == "__main__":
    # Crear clientes
    hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
    juan = Cliente(dni="22222222B", nombre="Juan", apellidos="Gonzalez Marquez")

    # Crear empresa con clientes iniciales
    empresa = Empresa(clientes=[hector, juan])

    # Mostrar todos los clientes
    print("==LISTADO DE CLIENTES==")
    for cliente in empresa.clientes:
        print(cliente)

    print("\n==MOSTRAR CLIENTES POR DNI==")
    empresa.mostrar_cliente("11111111A")  # Cliente existente
    empresa.mostrar_cliente("11111111Z")  # Cliente inexistente

    print("\n==BORRAR CLIENTES POR DNI==")
    empresa.borrar_cliente("22222222V")  # Cliente inexistente
    empresa.borrar_cliente("22222222B")  # Cliente existente

    print("\n==LISTADO DE CLIENTES==")
    for cliente in empresa.clientes:
        print(cliente)