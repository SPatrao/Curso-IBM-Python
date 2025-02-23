# EXCEPCIONES PERSONALIZADAS

# Definimos una clase para una excepción personalizada llamada 'EdadInvalidaError'
class EdadInvalidaError(Exception):
    """Excepción para edades inválidas"""
    
    # El constructor __init__ recibe dos parámetros:
    # - edad: la edad que se pasa como argumento al llamar la excepción
    # - mensaje: un mensaje personalizado que puede cambiarse (valor por defecto: "Edad no válida")
    def __init__(self, edad, mensaje="Edad no válida"):
        # Asignamos el valor de edad recibido
        self.edad = edad
        # Construimos el mensaje de error con el valor de edad
        self.mensaje = f"{mensaje}: {edad}"
        # Llamamos al constructor de la clase base Exception con el mensaje personalizado
        super().__init__(self.mensaje)

# Definimos una clase para una excepción personalizada llamada 'SaldoInsuficienteError'
class SaldoInsuficienteError(Exception):
    """Excepción para saldo insuficiente"""
    
    # El constructor __init__ recibe tres parámetros:
    # - saldo: el saldo actual de la cuenta
    # - monto: el monto que se intenta transferir
    # - mensaje: un mensaje personalizado que puede cambiarse (valor por defecto: "Saldo insuficiente")
    def __init__(self, saldo, monto, mensaje="Saldo insuficiente"):
        # Asignamos los valores de saldo y monto recibidos
        self.saldo = saldo
        self.monto = monto
        # Construimos el mensaje de error con los valores de saldo y monto
        self.mensaje = f"{mensaje}. Saldo: {saldo}, Monto: {monto}"
        # Llamamos al constructor de la clase base Exception con el mensaje personalizado
        super().__init__(self.mensaje)

# Función para validar la edad
def validar_edad(edad):
    """Validar rango de edad"""
    try:
        # Verificamos si la edad es menor que 0 o mayor que 120
        if edad < 0 or edad > 120:
            # Si la edad es fuera del rango, lanzamos una excepción 'EdadInvalidaError'
            raise EdadInvalidaError(edad)
        # Si la edad es válida, se imprime un mensaje de validación
        print(f"Edad válida: {edad}")
    # Capturamos la excepción 'EdadInvalidaError' si se lanza
    except EdadInvalidaError as e:
        # Imprimimos el mensaje de error generado por la excepción
        print(e)

# Función para simular una transferencia bancaria
def transferencia_bancaria(saldo_actual, monto):
    """Simular transferencia bancaria"""
    try:
        # Verificamos si el monto es mayor que el saldo actual
        if monto > saldo_actual:
            # Si el monto es mayor que el saldo, lanzamos una excepción 'SaldoInsuficienteError'
            raise SaldoInsuficienteError(saldo_actual, monto)
        # Si la transferencia es posible, actualizamos el saldo
        nuevo_saldo = saldo_actual - monto
        print(f"Transferencia realizada. Nuevo saldo: {nuevo_saldo}")
    # Capturamos la excepción 'SaldoInsuficienteError' si se lanza
    except SaldoInsuficienteError as e:
        # Imprimimos el mensaje de error generado por la excepción
        print(e)

# Punto de entrada principal del programa
if __name__ == "__main__":
    # Probamos la función validar_edad con una edad inválida (150)
    validar_edad(150)
    # Probamos la función validar_edad con una edad válida (25)
    validar_edad(25)
    # Probamos la función transferencia_bancaria con un saldo insuficiente
    transferencia_bancaria(100, 150)
    # Probamos la función transferencia_bancaria con una transferencia válida
    transferencia_bancaria(200, 50)
