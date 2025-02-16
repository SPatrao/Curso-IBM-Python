# EXCEPCIONES PERSONALIZADAS

class EdadInvalidaError(Exception):
    """Excepción para edades inválidas"""
    def __init__(self, edad, mensaje="Edad no válida"):
        self.edad = edad
        self.mensaje = f"{mensaje}: {edad}"
        super().__init__(self.mensaje)

class SaldoInsuficienteError(Exception):
    """Excepción para saldo insuficiente"""
    def __init__(self, saldo, monto, mensaje="Saldo insuficiente"):
        self.saldo = saldo
        self.monto = monto
        self.mensaje = f"{mensaje}. Saldo: {saldo}, Monto: {monto}"
        super().__init__(self.mensaje)

def validar_edad(edad):
    """Validar rango de edad"""
    try:
        if edad < 0 or edad > 120:
            raise EdadInvalidaError(edad)
        print(f"Edad válida: {edad}")
    except EdadInvalidaError as e:
        print(e)

def transferencia_bancaria(saldo_actual, monto):
    """Simular transferencia bancaria"""
    try:
        if monto > saldo_actual:
            raise SaldoInsuficienteError(saldo_actual, monto)
        nuevo_saldo = saldo_actual - monto
        print(f"Transferencia realizada. Nuevo saldo: {nuevo_saldo}")
    except SaldoInsuficienteError as e:
        print(e)

if __name__ == "__main__":
    validar_edad(150)
    validar_edad(25)
    transferencia_bancaria(100, 150)
    transferencia_bancaria(200, 50)

