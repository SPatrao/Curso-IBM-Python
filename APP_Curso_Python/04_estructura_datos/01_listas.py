# LISTAS EN PYTHON
# Las listas son colecciones de elementos en Python que pueden contener cualquier tipo de dato, como números, texto, etc.

# Creación de listas
# Una lista vacía no contiene ningún elemento.
lista_vacia = []

# Una lista con números enteros.
lista_numeros = [1, 2, 3, 4, 5]

# Una lista mixta, donde cada elemento puede ser de un tipo diferente: un número entero, una cadena de texto, un número decimal (flotante) y un valor booleano.
lista_mixta = [1, "texto", 3.14, True]

# Acceso a elementos
# Las listas en Python son indexadas, lo que significa que puedes acceder a los elementos usando su posición (índice). El índice comienza en 0.

# Acceder al primer elemento de la lista lista_numeros (índice 0)
print(lista_numeros[0])  # Esto imprimirá "1" ya que el primer elemento de la lista es 1.

# Acceder al último elemento de la lista lista_numeros. El índice -1 se usa para acceder al último elemento de la lista.
print(lista_numeros[-1])  # Esto imprimirá "5" porque 5 es el último elemento de la lista.

# Slicing (rebanado)
# El slicing permite obtener una parte de la lista, es decir, un subgrupo de elementos. La sintaxis es: lista[inicio:fin]

# Imprime los elementos de la lista desde el índice 1 hasta el índice 3 (sin incluir el índice 4)
print(lista_numeros[1:4])  # Esto imprimirá "[2, 3, 4]" porque los elementos en esas posiciones son 2, 3 y 4.

# Imprime los primeros tres elementos de la lista (índices 0, 1, 2)
print(lista_numeros[:3])   # Esto imprimirá "[1, 2, 3]".

# Imprime todos los elementos desde el índice 2 hasta el final de la lista
print(lista_numeros[2:])   # Esto imprimirá "[3, 4, 5]".

# Métodos de lista
# Los métodos son funciones predefinidas que puedes usar con listas. Algunos ejemplos son:

lista = [1, 2, 3, 4, 5]

# Añadir elementos
# El método append() agrega un elemento al final de la lista.
lista.append(6)  # Ahora la lista será: [1, 2, 3, 4, 5, 6]

# El método insert() inserta un elemento en una posición específica de la lista.
lista.insert(0, 0)  # Inserta el número 0 en el primer lugar de la lista. Ahora la lista es: [0, 1, 2, 3, 4, 5, 6]

# Eliminar elementos
# El método remove() elimina la primera aparición del valor especificado. Si hay varios elementos con el mismo valor, solo eliminará el primero.
lista.remove(3)  # Elimina el primer "3" de la lista. Ahora la lista es: [0, 1, 2, 4, 5, 6]

# El operador del elimina el elemento en la posición especificada por su índice.
del lista[1]  # Elimina el elemento en el índice 1 (el "1"). Ahora la lista es: [0, 2, 4, 5, 6]

# El método pop() elimina y devuelve el último elemento de la lista. Si no se especifica un índice, elimina el último.
ultimo = lista.pop()  # Elimina el último elemento, que es el "6", y lo guarda en la variable "ultimo".
print(ultimo)  # Imprime el valor "6" (el último elemento eliminado).

# Operaciones
# Puedes realizar algunas operaciones matemáticas con las listas.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# La concatenación de listas se puede hacer con el operador "+".
lista_concatenada = lista1 + lista2  # La lista resultante será: [1, 2, 3, 4, 5, 6]

# La repetición de listas se puede hacer con el operador "*".
lista_repetida = lista1 * 3  # La lista resultante será: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Funciones útiles
# Python proporciona varias funciones integradas para trabajar con listas.

# La función len() devuelve la longitud de la lista, es decir, cuántos elementos tiene.
print(len(lista))  # Esto imprimirá "5", ya que la lista tiene 5 elementos.

# La función max() devuelve el valor más grande en la lista.
print(max(lista))  # Esto imprimirá "5", que es el mayor número de la lista.

# La función min() devuelve el valor más pequeño en la lista.
print(min(lista))  # Esto imprimirá "0", que es el menor número de la lista.

# Ordenamiento
# Python tiene dos formas de ordenar las listas: sorted() y sort().

# sorted() devuelve una nueva lista ordenada sin modificar la lista original.
lista_desordenada = [3, 1, 4, 1, 5, 9, 2, 6]
lista_ordenada = sorted(lista_desordenada)  # Crea una nueva lista ordenada: [1, 1, 2, 3, 4, 5, 6, 9]
print(lista_ordenada)

# sort() ordena la lista original directamente, modificándola en su lugar.
lista_desordenada.sort()  # La lista original ahora está ordenada: [1, 1, 2, 3, 4, 5, 6, 9]
print(lista_desordenada)

# Invertir lista
# El método reverse() invierte el orden de los elementos en la lista original.
lista_desordenada.reverse()  # La lista ahora se verá: [9, 6, 5, 4, 3, 2, 1, 1]
print(lista_desordenada)

# Copiar listas
# Si necesitas una copia de una lista, puedes usar el método copy() para hacer una copia superficial o deepcopy() para una copia profunda (útil cuando la lista contiene otros objetos como listas dentro de listas).

# La copia superficial crea una nueva lista que es independiente de la original, pero no copia los objetos dentro de ella si hay listas u otros objetos.
copia_superficial = lista_desordenada.copy()

# La copia profunda se usa cuando quieres copiar todos los elementos, incluso si son objetos dentro de la lista (como sublistas).
import copy  # Necesitamos importar el módulo copy para usar deepcopy().
copia_profunda = copy.deepcopy(lista_desordenada)

# Comprensión de listas
# La comprensión de listas es una forma concisa y poderosa de crear listas.

# Crear una lista de los cuadrados de los números del 0 al 9 usando comprensión de listas.
cuadrados = [x**2 for x in range(10)]  # Esto crea una lista de los cuadrados: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Crear una lista con solo los números pares entre 0 y 9.
pares = [x for x in range(10) if x % 2 == 0]  # Esto crea una lista con los números pares: [0, 2, 4, 6, 8]

# Métodos de búsqueda
# Los métodos count() y index() permiten buscar elementos en una lista.

# La función count() devuelve cuántas veces aparece un valor en la lista.
print(lista_numeros.count(2))  # Esto imprimirá "1", ya que el número 2 aparece una vez en la lista.

# La función index() devuelve el índice de la primera aparición de un valor en la lista.
print(lista_numeros.index(3))  # Esto imprimirá "2", ya que el número 3 se encuentra en el índice 2 de la lista.
