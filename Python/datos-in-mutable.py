
# Obtener la dirección de memoria de una variable
  # En Python, los enteros son inmutables, por lo que su dirección de memoria puede cambiar si su valor cambia
a = 65
print("La dirección de memoria de 'a' es:", id(a))

# Obtener la dirección de memoria de una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero  # Ambas variables apuntan al mismo valor en memoria
print("La dirección de memoria de 'miNumero' es:", id(miNumero))
print("La dirección de memoria de 'miNumero2' es:", id(miNumero2))  # Misma dirección

# Si cambio el valor de la variable, se crea un nuevo objeto en otra dirección de memoria
a = 65
print("La dirección de memoria de 'a' es:", id(a))
a += 2  # Al modificar su valor, se crea un nuevo objeto en memoria
print("Después de modificar 'a', la nueva dirección de memoria es:", id(a))

# Obtener la dirección de memoria de una tupla
miTupla = (1, 2, 3, 4, 5)
print("La dirección de memoria de 'miTupla' es:", id(miTupla))

# Obtener la dirección de memoria de una lista
miLista = [1, 2, 3, 4, 5]
print("La dirección de memoria de 'miLista' es:", id(miLista))

# Obtener la dirección de memoria de un diccionario
diccionario = {'a': 1, 'b': 2}
print("Contenido inicial del diccionario:", diccionario)
print("La dirección de memoria de 'diccionario' es:", id(diccionario))

diccionario["c"] = 3  # Se modifica el diccionario
print("Contenido actualizado del diccionario:", diccionario)
print("La dirección de memoria de 'diccionario' tras la modificación es:", id(diccionario))

# Ejemplo con una lista mutable
miLista2 = [1, 2, 3]
print("La dirección de memoria de 'miLista2' inicial es:", id(miLista2))

# Agregar un elemento a la lista
miLista2.append(4)
print("Después de agregar un elemento, la dirección de memoria de 'miLista2' es:", id(miLista2))

# Ejemplo con una cadena inmutable
miCadena = "Hola"
print("La dirección de memoria de 'miCadena' inicial es:", id(miCadena))

# Modificar la cadena
miCadena += " Mundo"
print("Después de modificar la cadena, la nueva dirección de memoria de 'miCadena' es:", id(miCadena))

# Ejemplo con un objeto personalizado (clase)
class MiClase:
    def __init__(self, valor):
        self.valor = valor

objeto = MiClase(10)
print("La dirección de memoria del objeto 'MiClase' inicial es:", id(objeto))

# Modificar el atributo del objeto
objeto.valor = 20
print("Después de modificar el atributo, la nueva dirección de memoria del objeto es:", id(objeto))