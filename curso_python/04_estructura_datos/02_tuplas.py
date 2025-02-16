# TUPLAS EN PYTHON
# Una tupla es una colección ordenada e inmutable de elementos. 
# Esto significa que una vez que creas una tupla, no puedes cambiar sus elementos, lo que la hace más segura que las listas en algunos casos.

# CREACIÓN DE TUPLAS
# Puedes crear una tupla simplemente usando paréntesis () y separando los elementos con comas.
tupla_vacia = ()  # Una tupla vacía, que no contiene ningún elemento.
tupla_numeros = (1, 2, 3, 4, 5)  # Una tupla que contiene números enteros.
tupla_mixta = (1, "texto", 3.14, True)  # Una tupla que contiene diferentes tipos de datos: un número, una cadena de texto, un flotante y un valor booleano.

# ACCESO A ELEMENTOS EN UNA TUPLA
# Puedes acceder a los elementos de una tupla de manera similar a las listas, usando índices. Los índices comienzan en 0 para el primer elemento.
# Acceder al primer elemento de la tupla tupla_numeros.
print(tupla_numeros[0])  # Esto imprime el primer elemento, que es "1".

# Puedes usar índices negativos para acceder a los elementos desde el final de la tupla.
# Acceder al último elemento de la tupla.
print(tupla_numeros[-1])  # Esto imprime el último elemento, que es "5".

# SLICING (REBANADO)
# El slicing es una técnica que te permite acceder a un subconjunto de elementos de una tupla.
# El formato básico para hacer slicing es: tupla[inicio:fin], donde "inicio" es el índice desde donde quieres empezar y "fin" es el índice hasta donde quieres cortar (pero no incluye ese índice).
print(tupla_numeros[1:4])  # Esto imprime los elementos desde el índice 1 hasta el índice 3, es decir, [2, 3, 4].

# CARACTERÍSTICAS DE LAS TUPLAS (INMUTABILIDAD)
# A diferencia de las listas, las tuplas son inmutables. Esto significa que no puedes cambiar un elemento después de crear la tupla.
# Por ejemplo, la siguiente línea de código generaría un error porque estamos tratando de modificar un elemento de la tupla.
# tupla_numeros[0] = 10  # Esto generaría un error porque las tuplas no pueden ser modificadas.

# CONVERSIÓN DE UNA LISTA A UNA TUPLA
# Si tienes una lista y quieres convertirla en una tupla, puedes usar la función tuple().
lista = [1, 2, 3]  # Una lista que contiene tres elementos.
tupla = tuple(lista)  # Convierte la lista en una tupla. Ahora, tupla será (1, 2, 3).

# DESEMPAQUETADO DE TUPLAS
# El desempaquetado de tuplas te permite asignar los elementos de una tupla a variables individuales en una sola línea.
# Por ejemplo, si tienes una tupla con tres elementos, puedes asignar cada uno a una variable.
a, b, c = tupla_numeros  # La tupla (1, 2, 3, 4, 5) se desempaqueta en tres variables: a = 1, b = 2, c = 3.

# MÉTODOS DE TUPLAS
# Las tuplas tienen algunos métodos útiles que puedes usar.

# El método count() cuenta cuántas veces aparece un elemento en la tupla.
print(tupla_numeros.count(2))  # Esto imprime "1", porque el número "2" aparece una vez en la tupla.

# El método index() devuelve el índice de la primera aparición de un valor en la tupla.
print(tupla_numeros.index(3))  # Esto imprime "2", ya que el valor "3" se encuentra en el índice 2 de la tupla.

# CONCATENACIÓN DE TUPLAS
# Al igual que con las listas, puedes concatenar (unir) dos o más tuplas usando el operador "+".
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2  # Esto crea una nueva tupla que contiene todos los elementos de tupla1 seguidos de los elementos de tupla2.
print(tupla_concatenada)  # Imprime: (1, 2, 3, 4, 5, 6)

# REPETICIÓN DE TUPLAS
# Puedes repetir una tupla un número específico de veces usando el operador "*".
tupla_repetida = tupla1 * 3  # Esto crea una nueva tupla que contiene tupla1 repetida tres veces.
print(tupla_repetida)  # Imprime: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# FUNCIONES ÚTILES PARA TUPLAS
# Python proporciona varias funciones integradas para trabajar con tuplas.

# La función len() devuelve el número de elementos de una tupla.
print(len(tupla_numeros))  # Imprime: 5, porque la tupla tiene 5 elementos.

# La función max() devuelve el valor más grande de la tupla (en este caso, el valor numérico más grande).
print(max(tupla_numeros))  # Imprime: 5, porque el valor máximo en la tupla es 5.

# La función min() devuelve el valor más pequeño de la tupla.
print(min(tupla_numeros))  # Imprime: 1, porque el valor mínimo en la tupla es 1.

# TUPLAS COMO CLAVES DE UN DICCIONARIO
# Las tuplas son inmutables, lo que las convierte en un tipo de dato adecuado para usar como claves de un diccionario.
# Los diccionarios en Python permiten usar claves para acceder a valores asociados.
diccionario = {
    (1, 2): "Coordenada 1,2",
    (3, 4): "Coordenada 3,4"
}  # Las tuplas (1, 2) y (3, 4) se utilizan como claves en el diccionario.

# TUPLAS DE UN SOLO ELEMENTO
# Si quieres crear una tupla que contenga solo un elemento, debes colocar una coma después del elemento.
# Esto es necesario porque de lo contrario Python lo interpretaría como un valor normal entre paréntesis.
tupla_un_elemento = (1,)  # Esto crea una tupla con un solo elemento: (1).
print(tupla_un_elemento)  # Imprime: (1)
