from django.http import HttpResponse
from datetime import date  # Importa la clase date directamente
from .models import Cliente, Factura

# Vista para mostrar un saludo
def saludo(request):
    texto = """
    <html>
        <head>
            <title>Saludo</title>
        </head>
        <body>
            <h1>Hola, este es un saludo desde Django</h1>
            <h2>saludo desde Django h2</h2>
            <p>Este es un párrafo</p>
        </body>
    </html>"""
    return HttpResponse(texto)

# Vista para mostrar la fecha actual
def fecha(request):
    miFecha = date.today()  # Obtiene la fecha actual
    texto2 = """
    <html>
    <body>
    <h2>Fecha y hora actual: </h2>%s
    </body>
    </html>
    """ % miFecha
    return HttpResponse(texto2)

# Vista para calcular la edad futura
def calcEdad(request, year):
    edadActual = 40
    periodo = year - 2025
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años.</h2></body></html>" % (year, edadFutura)
    return HttpResponse(documento)

# Vista para calcular la edad futura con una edad inicial dada
def calcEdad2(request, edadActual, year):
    periodo = year - 2025
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años.</h2></body></html>" % (year, edadFutura)
    return HttpResponse(documento)

# Vista para crear un cliente y una factura (solo para demostración)
def crear_cliente(request):
    # Verificar si el cliente ya existe
    rfc = "AGRM-801205-400"
    if Cliente.objects.filter(rfc=rfc).exists():
        return HttpResponse("El cliente ya existe en la base de datos.")

    # Crear el cliente si no existe
    fecha_nacimiento = date(1980, 12, 5)
    pedro = Cliente(
        nombre="Pedro",
        apellidos="Aguilar Ramírez",
        rfc=rfc,
        fecha_nacimiento=fecha_nacimiento,
        activo=True,
    )
    pedro.save()

    # Crear la factura asociada al cliente
    factura = Factura(cliente=pedro, importe=5690.12, pagada=False)
    factura.save()

    # Usando el método create()
    pedro = Cliente.objects.create(
        nombre="Angel",
        apellidos="Martin Ramírez",
        rfc="AGRM-801410-987",
        fecha_nacimiento=fecha_nacimiento,
        activo=True,
    )
    factura = Factura.objects.create(cliente=pedro, importe=9999.99, pagada=False)

    return HttpResponse("Cliente y factura creados exitosamente.")
