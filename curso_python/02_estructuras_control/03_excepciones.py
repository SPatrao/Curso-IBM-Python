# MANEJO DE EXCEPCIONES EN PYTHON

# 1. Bloque try-except básico
# En Python, las excepciones son errores que ocurren durante la ejecución del programa.
# Usamos el bloque 'try' para intentar ejecutar código que puede generar un error, y el bloque 'except' para capturar y manejar ese error.
try:
    x = 10 / 0  # Intentamos dividir 10 entre 0, lo cual genera un error (ZeroDivisionError)
except ZeroDivisionError:  # Capturamos específicamente el error de división por cero
    print("No se puede dividir por cero")  # Mostramos un mensaje si ocurre el error

# 2. Múltiples excepciones
# Aquí se muestran dos tipos de excepciones: 'ValueError' y 'ZeroDivisionError'.
# El bloque 'except' puede manejar múltiples excepciones con diferentes bloques.
try:
    numero = int(input("Ingresa un número: "))  # Pedimos al usuario ingresar un número
    resultado = 10 / numero  # Intentamos dividir 10 entre el número que el usuario ingresó
except ValueError:  # Capturamos si el usuario ingresa algo que no se pueda convertir a un número
    print("Entrada inválida. Debes ingresar un número.")
except ZeroDivisionError:  # Capturamos si el usuario intenta dividir por cero
    print("No se puede dividir por cero")

# 3. Capturar cualquier excepción
# En este bloque, se captura cualquier tipo de error usando 'Exception' como clase base para excepciones.
try:
    # Intentamos convertir una cadena de texto que no es un número en un número entero
    valor = int("texto")  # Esto generará un error de tipo ValueError
except Exception as error:  # Capturamos cualquier excepción y la almacenamos en 'error'
    print(f"Ocurrió un error: {error}")  # Mostramos el mensaje del error

# 4. Bloque else
# El bloque 'else' se ejecuta solo si no ocurrió ninguna excepción en el bloque 'try'.
try:
    numero = int(input("Ingresa un número: "))  # Solicitamos un número al usuario
except ValueError:  # Si el usuario ingresa algo que no es un número, atrapamos la excepción
    print("Entrada inválida")  # Mostramos un mensaje de error
else:  # Si no hay excepción (el usuario ingresa un número válido), ejecutamos este bloque
    print("El número ingresado es:", numero)  # Imprimimos el número ingresado

# 5. Bloque finally
# El bloque 'finally' se ejecuta siempre, sin importar si hubo o no una excepción en el bloque 'try'.
try:
    archivo = open("ejemplo.txt", "r")  # Intentamos abrir un archivo
    # Aquí irían operaciones con el archivo, pero si no se encuentra el archivo, genera un error.
except FileNotFoundError:  # Si el archivo no existe, capturamos el error
    print("El archivo no existe")
finally:  # Este bloque se ejecuta siempre, incluso si hubo un error o no
    archivo.close()  # Cerramos el archivo, asegurándonos de que no quede abierto, aunque no exista.

# 6. Lanzar excepciones propias
# Podemos crear nuestras propias excepciones usando la palabra clave 'raise'.
def dividir(a, b):
    if b == 0:  # Si 'b' es igual a cero, no podemos dividir
        raise ValueError("No se puede dividir por cero")  # Lanza un error 'ValueError' con un mensaje personalizado
    return a / b  # Si no hay error, realizamos la división y devolvemos el resultado

try:
    resultado = dividir(10, 0)  # Intentamos dividir 10 entre 0, lo que generará una excepción
except ValueError as error:  # Capturamos el 'ValueError' lanzado
    print(error)  # Mostramos el mensaje del error: "No se puede dividir por cero"

# 7. Crear excepciones personalizadas
# Podemos crear nuestras propias excepciones definidas por el usuario. Para ello, heredamos de la clase 'Exception'.
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):  # El constructor inicializa el mensaje de la excepción
        self.mensaje = mensaje  # Asignamos el mensaje recibido como atributo
        super().__init__(self.mensaje)  # Llamamos al constructor de la clase base 'Exception' para asegurarnos de que se maneje correctamente.

try:
    edad = -5  # Definimos una edad negativa, lo que es un error lógico
    if edad < 0:  # Si la edad es negativa, lanzamos una excepción personalizada
        raise MiExcepcionPersonalizada("La edad no puede ser negativa")  # Lanzamos la excepción con un mensaje personalizado
except MiExcepcionPersonalizada as error:  # Capturamos nuestra excepción personalizada
    print(error)  # Mostramos el mensaje: "La edad no puede ser negativa"
