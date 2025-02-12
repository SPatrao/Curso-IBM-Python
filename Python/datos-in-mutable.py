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
# Las tuplas son inmutables, por lo que su dirección de memoria no cambia
miTupla = (1, 2, 3, 4, 5)
print("La dirección de memoria de 'miTupla' es:", id(miTupla))

# Obtener la dirección de memoria de una lista
# Las listas son mutables, por lo que su dirección de memoria se mantiene aunque se modifiquen
miLista = [1, 2, 3, 4, 5]
print("La dirección de memoria de 'miLista' es:", id(miLista))

# Obtener la dirección de memoria de un diccionario
# Los diccionarios también son mutables, así que mantienen su dirección de memoria al modificarse
diccionario = {'a': 1, 'b': 2}
print("Contenido inicial del diccionario:", diccionario)
print("La dirección de memoria de 'diccionario' es:", id(diccionario))

diccionario["c"] = 3  # Se modifica el diccionario
print("Contenido actualizado del diccionario:", diccionario)
print("La dirección de memoria de 'diccionario' tras la modificación es:", id(diccionario))
