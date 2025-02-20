# EXCEPCIONES PERSONALIZADAS EN PYTHON
# ======================================
# Objetivo: Mostrar cómo crear y manejar excepciones personalizadas en Python.
# Este archivo cubre la creación de excepciones propias y su uso en la validación de datos.

# 1. Función para lanzar excepciones propias
def dividir(a, b):
    """Función que divide dos números.

    Args:
        a (int o float): El numerador de la operación.
        b (int o float): El denominador de la operación.

    Raises:
        ValueError: Si se intenta dividir por cero.

    Returns:
        float: Resultado de la división.
    """
    if b == 0:  # Verificamos si el denominador es cero
        raise ValueError("No se puede dividir por cero")  # Lanza una excepción ValueError con un mensaje personalizado
    return a / b  # Devuelve el resultado de la división

# Ejemplo de uso de la función dividir
try:
    resultado = dividir(10, 0)  # Intentamos dividir 10 entre 0
except ValueError as error:  # Capturamos el error lanzado
    print(f"Error: {error}")  # Mostramos el mensaje del error en caso de excepción

# 2. Crear excepciones personalizadas
class MiExcepcionPersonalizada(Exception):
    """Clase de excepción personalizada que hereda de la clase Exception."""

    def __init__(self, mensaje):
        """Inicializa la excepción con un mensaje.

        Args:
            mensaje (str): Mensaje de la excepción.
        """
        self.mensaje = mensaje  # Asignamos el mensaje como atributo
        super().__init__(self.mensaje)  # Llamamos al inicializador de la clase base

# Ejemplo de validación de edad
print("\n🔹 Validación de Edad:")
while True:  # Bucle para pedir la edad
    try:
        edad = int(input("Ingresa tu edad: "))  # Solicitamos la edad al usuario
        if edad < 0:  # Verificamos si la edad es negativa
            raise MiExcepcionPersonalizada("La edad no puede ser negativa")  # Lanzamos nuestra excepción personalizada
        break  # Si todo está bien, salimos del bucle
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")  # Mensaje si la entrada no es válida
    except MiExcepcionPersonalizada as error:
        print(f"Error: {error}")  # Mensaje de nuestra excepción personalizada

print(f"Edad ingresada: {edad}")  # Imprimimos la edad validada

# EJERCICIOS FINALES
# ======================================
print("\n🔹 Ejercicios Finales:")

# Ejercicio 1: Crear un programa que utilice la función dividir, manejando errores.
try:
    numerador = float(input("Ingresa el numerador: "))  #Entrada del numerador
    denominador = float(input("Ingresa el denominador: "))  #Entrada del denominador
    resultado_division = dividir(numerador, denominador)  # Intentamos dividir
    print(f"El resultado de dividir {numerador} entre {denominador} es: {resultado_division}")  # Resultado de la división
except Exception as error:
    print(f"Error: {error}")  # Mensaje si ocurre cualquier error

# Ejercicio 2: Validar la edad con condiciones adicionales.
while True:  # Bucle para pedir la edad
    try:
        edad = int(input("Ingresa tu edad: "))  # Solicitamos la edad
        if edad < 0:
            raise MiExcepcionPersonalizada("La edad no puede ser negativa.")  # Lanzar excepción si es negativa
        elif edad > 150:
            raise MiExcepcionPersonalizada("La edad no puede ser mayor a 150 años.")  # Lanzar excepción si supera 150
        break  # Si todo está bien, salir del bucle
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")  # Error en caso de tipo incorrecto
    except MiExcepcionPersonalizada as error:
        print(f"Error: {error}")  # Mensaje de nuestra excepción personalizada

print(f"Edad válida ingresada: {edad}")  # Impriir la edad válida

