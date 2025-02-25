
class SalaCine:
    # Constructor de la clase SalaCine
    def __init__(self):
        # Lista privada para almacenar los asientos de la sala
        self._asientos = []
        
        # Precio base para las entradas
        self._precio_base = 10

    # Método para agregar un nuevo asiento a la sala
    def agregar_asiento(self, asiento):
        # Verificamos si el asiento ya existe para evitar duplicados
        if self.buscar_asiento(asiento.get_numero(), asiento.get_fila()):
            # Lanzamos una excepción si el asiento ya existe
            raise ValueError("El asiento ya existe")
        
        # Si no existe, lo agregamos a la lista de asientos
        self._asientos.append(asiento)

    # Método para reservar un asiento
    def reservar_asiento(self, numero, fila, edad, dia):
        # Buscamos el asiento por su número y fila
        asiento = self.buscar_asiento(numero, fila)
        
        # Validaciones antes de reservar
        if not asiento:
            # Lanzamos excepción si no se encuentra el asiento
            raise ValueError("Asiento no encontrado")
        
        if asiento.is_reservado():
            # Lanzamos excepción si el asiento ya está reservado
            raise ValueError("El asiento ya está reservado")

        # Calculamos el precio según edad y día
        precio = self.calcular_precio(edad, dia)
        
        # Establecemos el precio y marcamos como reservado
        asiento.set_precio(precio)
        asiento.set_reservado(True)

    # Método para cancelar la reserva de un asiento
    def cancelar_reserva(self, numero, fila):
        # Buscamos el asiento
        asiento = self.buscar_asiento(numero, fila)
        
        # Validaciones antes de cancelar
        if not asiento:
            raise ValueError("Asiento no encontrado")
        
        if not asiento.is_reservado():
            raise ValueError("El asiento no está reservado")

        # Marcamos el asiento como no reservado
        asiento.set_reservado(False)

    # Método para mostrar el estado de todos los asientos
    def mostrar_asientos(self):
        for asiento in self._asientos:
            # Imprimimos detalles de cada asiento
            print(f"Asiento {asiento.get_numero()}, Fila {asiento.get_fila()}: "
                  f"{'Reservado' if asiento.is_reservado() else 'Disponible'}, "
                  f"Precio: {asiento.get_precio()}")

    # Método para buscar un asiento específico
    def buscar_asiento(self, numero, fila):
        # Recorremos la lista de asientos
        for asiento in self._asientos:
            # Buscamos el asiento que coincida con número y fila
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        
        # Retornamos None si no se encuentra
        return None

    # Método para calcular el precio con descuentos
    def calcular_precio(self, edad, dia):
        # Comenzamos con el precio base
        precio = self._precio_base

        # Descuento de día del espectador (miércoles)
        if dia == "miercoles":
            precio *= 0.8  # 20% de descuento

        # Descuento para mayores de 65 años
        if edad > 65:
            precio *= 0.7  # 30% de descuento
        return precio
    

class Asiento:
    # Constructor de la clase Asiento
    def __init__(self, numero, fila):
        # Atributos protegidos (convención con guión bajo)
        
        # Número único del asiento en la sala
        self._numero = numero
        
        # Fila a la que pertenece el asiento
        self._fila = fila
        
        # Estado de reserva del asiento (inicialmente no reservado)
        self._reservado = False
        
        # Precio del asiento (inicialmente 0)
        self._precio = 0

    # Métodos Getter y Setter: Proporcionan acceso controlado a los atributos privados

    # Obtener el número del asiento
    def get_numero(self):
        return self._numero

    # Obtener la fila del asiento
    def get_fila(self):
        return self._fila

    # Verificar si el asiento está reservado
    def is_reservado(self):
        return self._reservado

    # Establecer el estado de reserva del asiento
    def set_reservado(self, reservado):
        self._reservado = reservado

    # Obtener el precio del asiento
    def get_precio(self):
        return self._precio

    # Establecer el precio del asiento
    def set_precio(self, precio):
        self._precio = precio


sala = SalaCine()

# Agregar asientos
sala.agregar_asiento(Asiento(1, 1))
sala.agregar_asiento(Asiento(1, 2))
sala.agregar_asiento(Asiento(1, 3))
sala.agregar_asiento(Asiento(2, 1))
sala.agregar_asiento(Asiento(2, 2))
sala.agregar_asiento(Asiento(2, 3))
sala.agregar_asiento(Asiento(3, 1))
sala.agregar_asiento(Asiento(3, 2))
sala.agregar_asiento(Asiento(3, 3))

# Reservar asientos
sala.reservar_asiento(1, 1, 30, "lunes")
sala.reservar_asiento(2, 1, 70, "miercoles")
sala.reservar_asiento(3, 1, 30, "martes")
sala.reservar_asiento(3, 2, 70, "miercoles")

# Mostrar asientos después de reservar
sala.mostrar_asientos()


# Función para mostrar el menú principal
def mostrar_menu():
    """
    Despliega las opciones disponibles en el sistema de reservas
    Proporciona una interfaz de usuario clara y estructurada
    """
    print("\n--- Sistema de Reservas de Cine ---")
    print("1. Mostrar asientos")      # Visualizar estado actual de asientos
    print("2. Reservar asiento")       # Realizar nueva reserva
    print("3. Cancelar reserva")       # Eliminar reserva existente
    print("4. Buscar asiento")         # Consultar detalles de un asiento
    print("5. Salir")                  # Terminar el programa


def obtener_entrada_numerica(mensaje):
    """
    Función de validación para entradas numéricas
    
    Características:
    - Manejo de excepciones para entradas no numéricas
    - Bucle infinito hasta obtener entrada válida
    - Muestra mensaje de error en caso de entrada inválida
    
    Parámetros:
    - mensaje: Texto que se muestra para solicitar la entrada
    
    Retorna:
    - Valor numérico ingresado por el usuario
    """
    while True:
        try:
            # Intenta convertir la entrada a entero
            return int(input(mensaje))
        except ValueError:
            # Captura error si la entrada no es un número
            print("Entrada inválida. Debe ser un número.")



def obtener_dia():
    """
    Función para validar el día de la semana
    
    Características:
    - Solicita ingreso de día
    - Convierte a minúsculas para comparación
    - Valida contra lista predefinida de días
    
    Retorna:
    - Día válido ingresado por el usuario
    """
    while True:
        # Solicitar día e convertir a minúsculas
        dia = input("Ingrese el día (lunes, martes, miercoles, jueves, viernes, sabado, domingo): ").lower()
        
        # Lista de días válidos
        dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        
        # Validar si el día está en la lista
        if dia in dias_validos:
            return dia
        
        # Mensaje de error si el día no es válido
        print("Día inválido.")

while True:
    # Mostrar menú en cada iteración
    mostrar_menu()
    
    # Obtener opción del usuario
    opcion = obtener_entrada_numerica("Seleccione una opción: ")

    # Estructura de control con múltiples opciones
    if opcion == 1:
        # Opción 1: Mostrar asientos
        sala.mostrar_asientos()

    elif opcion == 2:
        # Opción 2: Reservar asiento
        # Solicitar detalles de reserva
        numero = obtener_entrada_numerica("Ingrese el número de asiento: ")
        fila = obtener_entrada_numerica("Ingrese la fila del asiento: ")
        edad = obtener_entrada_numerica("Ingrese la edad del espectador: ")
        dia = obtener_dia()

        try:
            # Intentar realizar reserva
            sala.reservar_asiento(numero, fila, edad, dia)
            print("Reserva realizada con éxito.")
        except ValueError as e:
            # Capturar y mostrar errores de reserva
            print(f"Error: {e}")

    elif opcion == 3:
        # Opción 3: Cancelar reserva
        numero = obtener_entrada_numerica("Ingrese el número de asiento a cancelar: ")
        fila = obtener_entrada_numerica("Ingrese la fila del asiento a cancelar: ")

        try:
            # Intentar cancelar reserva
            sala.cancelar_reserva(numero, fila)
            print("Reserva cancelada con éxito.")
        except ValueError as e:
            # Capturar y mostrar errores de cancelación
            print(f"Error: {e}")

    elif opcion == 4:
        # Opción 4: Buscar asiento
        numero = obtener_entrada_numerica("Ingrese el número de asiento a buscar: ")
        fila = obtener_entrada_numerica("Ingrese la fila del asiento a buscar: ")

        # Buscar asiento y mostrar resultado
        asiento = sala.buscar_asiento(numero, fila)
        if asiento:
            print(f"Asiento encontrado: Número {asiento.get_numero()}, Fila {asiento.get_fila()}")
            print(f"{'Reservado' if asiento.is_reservado() else 'Disponible'}")
        else:
            print("Asiento no encontrado.")

    elif opcion == 5:
        # Opción 5: Salir del programa
        break

    else:
        # Manejar opciones inválidas
        print("Opción inválida.")