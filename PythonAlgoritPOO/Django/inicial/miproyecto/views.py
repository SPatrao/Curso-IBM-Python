
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def saludo(request):
    #return HttpResponse("Hello, this is your response!")
    #eturn HttpResponse("<html><head><title>Page not found</title></head><body><h1>Page not found</h1><p>The requested URL was not found on this server.</p></body></html>")
    #texto = "<html><head><title>Saludo</title></head><body><h1>Hola, este es un saludo desde Django</h1></body></html>"
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
    
def fecha(request):
    miFecha=datetime.now()
    texto2 = """
    <html>
    <body>
    <h2>Fecha y hora actual: </h2>%s
    </body>
    </html>
    """ % miFecha
    return HttpResponse(texto2)

from django.http import HttpResponse

def calcEdad(request, year):
    edadActual = 40
    periodo = year - 2025
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años.</h2></body></html>" % (year, edadFutura)
    return HttpResponse(documento)

def calcEdad2(request, edadActual, year):
    periodo=year-2025
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s años.</h2></body></html>" % (year, edadFutura)
    return HttpResponse(documento)
