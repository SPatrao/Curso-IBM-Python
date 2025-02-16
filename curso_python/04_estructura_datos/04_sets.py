# CONJUNTOS (SETS) EN PYTHON

# Creación de sets
# Un conjunto (set) es una colección de elementos no ordenados y sin elementos duplicados.
# Se crean con llaves {}, pero a diferencia de los diccionarios, no necesitan tener claves.
set_vacio = set()  # Un conjunto vacío se crea usando la función set()

# Un conjunto con algunos números
set_numeros = {1, 2, 3, 4, 5}  # Un set con números del 1 al 5

# Un conjunto con elementos de diferentes tipos (enteros, cadenas, flotantes)
set_mixto = {1, "texto", 3.14}  # Un set puede contener elementos de diferentes tipos de datos

# Características
# - No hay elementos duplicados: Si intentas agregar un elemento ya existente, el set no lo incluirá.
# - No tienen orden específico: Los elementos en un set no tienen un índice como las listas, lo que significa que no puedes acceder a ellos por su posición.

# Crear un set a partir de una lista
# Si tienes una lista con elementos duplicados, puedes convertirla en un set para eliminar los duplicados automáticamente.
lista = [1, 2, 2, 3, 3, 4]  # Lista con elementos duplicados
set_desde_lista = set(lista)  # El set resultante será {1, 2, 3, 4}, ya que elimina los duplicados

# Operaciones básicas entre sets
set1 = {1, 2, 3, 4}  # Un conjunto con elementos del 1 al 4
set2 = {3, 4, 5, 6}  # Otro conjunto con elementos del 3 al 6

# Unión: La unión de dos sets devuelve un nuevo set con todos los elementos de ambos sets, sin duplicados.
union = set1.union(set2)  # Unión de set1 y set2, el resultado será {1, 2, 3, 4, 5, 6}
union_alternativa = set1 | set2  # Otra forma de hacer la unión usando el operador '|'

# Intersección: La intersección de dos sets devuelve un nuevo set con los elementos comunes a ambos sets.
interseccion = set1.intersection(set2)  # Intersección de set1 y set2, el resultado será {3, 4}
interseccion_alternativa = set1 & set2  # Otra forma de hacer la intersección usando el operador '&'

# Diferencia: La diferencia de dos sets devuelve un nuevo set con los elementos de set1 que no están en set2.
diferencia = set1.difference(set2)  # Elementos de set1 que no están en set2, el resultado será {1, 2}
diferencia_alternativa = set1 - set2  # Otra forma de hacer la diferencia usando el operador '-'

# Diferencia simétrica: Devuelve un nuevo set con los elementos que están en uno de los sets, pero no en ambos.
diferencia_simetrica = set1.symmetric_difference(set2)  # El resultado será {1, 2, 5, 6}
diferencia_simetrica_alternativa = set1 ^ set2  # Otra forma de hacer la diferencia simétrica usando el operador '^'

# Métodos de modificación
# Los sets son mutables, lo que significa que puedes modificarlos después de haberlos creado.

set_numeros.add(6)  # Añadir un nuevo elemento al set. El set se convierte en {1, 2, 3, 4, 5, 6}

set_numeros.remove(3)  # Eliminar un elemento del set. El set se convierte en {1, 2, 4, 5, 6}
# Si intentas eliminar un elemento que no existe en el set, Python lanzará un KeyError.

set_numeros.discard(7)  # Eliminar un elemento sin error si no existe. En este caso, 7 no está en el set, pero no ocurre ningún error.
# discard() es útil cuando no estás seguro si el elemento está presente.

# Operaciones de pertenencia
# Puedes verificar si un elemento está en un set usando el operador 'in', que devuelve True o False.

print(2 in set_numeros)  # Verifica si el número 2 está en set_numeros, devuelve True porque 2 está en el set

# Copiar sets
# Si necesitas hacer una copia de un set para no modificar el original, puedes usar el método copy().
copia_set = set_numeros.copy()  # Crea una copia superficial del set set_numeros

# Limpiar un set
# Si quieres eliminar todos los elementos de un set, puedes usar el método clear().
set_numeros.clear()  # Vacía el set, ahora set_numeros es un set vacío {}

# Subconjuntos y superconjuntos
# Un conjunto es un subconjunto de otro si todos sus elementos están en el otro conjunto.
# Un conjunto es un superconjunto de otro si contiene todos los elementos del otro conjunto.

set_a = {1, 2, 3}  # Un conjunto con los elementos 1, 2 y 3
set_b = {1, 2}     # Un conjunto con los elementos 1 y 2

# El método 'issubset()' verifica si un conjunto es subconjunto de otro.
print(set_b.issubset(set_a))  # Devuelve True, porque todos los elementos de set_b están en set_a

# El método 'issuperset()' verifica si un conjunto es superconjunto de otro.
print(set_a.issuperset(set_b))  # Devuelve True, porque todos los elementos de set_b están en set_a
