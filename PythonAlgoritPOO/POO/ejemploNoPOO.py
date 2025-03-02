#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definimos una lista de clientes, donde cada cliente es un diccionario con Nombre, Apellidos y DNI
clientes = [
    {'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'},
    {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}
]


# Creamos una función para mostrar un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    """
    Esta función busca un cliente por DNI en la lista de clientes e imprime su nombre y apellidos.
    Si no encuentra el cliente, imprime un mensaje indicando que no se encontró.

    Args:
        clientes (list): Una lista de diccionarios, donde cada diccionario representa un cliente.
        dni (str): El DNI del cliente que se quiere mostrar.

    Returns:
        None
    """
    for c in clientes:  # Iteramos sobre cada cliente en la lista
        if dni == c['dni']:  # Comparamos el DNI proporcionado con el DNI del cliente actual
            print('{} {}'.format(c['Nombre'], c['Apellidos']))  # Imprimimos el nombre y apellidos del cliente si coincide
            return  # Salimos de la función después de encontrar y mostrar el cliente
    print('Cliente no encontrado')  # Imprimimos este mensaje si no se encuentra ningún cliente con el DNI proporcionado


# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    """
    Esta función busca un cliente por DNI en la lista de clientes y lo elimina.
    Si encuentra el cliente, lo elimina de la lista e imprime un mensaje indicando que fue borrado.
    Si no encuentra el cliente, imprime un mensaje indicando que no se encontró.

    Args:
        clientes (list): Una lista de diccionarios, donde cada diccionario representa un cliente.
        dni (str): El DNI del cliente que se quiere borrar.

    Returns:
        None
    """
    for i, c in enumerate(clientes):  # Iteramos sobre cada cliente en la lista, obteniendo el índice y el cliente
        if dni == c['dni']:  # Comparamos el DNI proporcionado con el DNI del cliente actual
            del clientes[i]  # Eliminamos el cliente de la lista usando su índice
            print(str(c), "> BORRADO")  # Imprimimos un mensaje indicando que el cliente fue borrado
            return  # Salimos de la función después de borrar el cliente
    print('Cliente no encontrado')  # Imprimimos este mensaje si no se encuentra ningún cliente con el DNI proporcionado


def agregar_cliente(clientes, nombre, apellidos, dni):
    """
    Esta función agrega un nuevo cliente a la lista de clientes, verificando que el DNI no exista previamente.

    Args:
        clientes (list): La lista de diccionarios donde se almacenan los clientes.
        nombre (str): El nombre del nuevo cliente.
        apellidos (str): Los apellidos del nuevo cliente.
        dni (str): El DNI del nuevo cliente.

    Returns:
        None
    """
    # Validar que el DNI no exista ya
    for cliente in clientes:
        if cliente['dni'] == dni:
            print("Error: Ya existe un cliente con ese DNI.")
            return

    # Validar que los campos no estén vacíos
    if not nombre or not apellidos or not dni:
        print("Error: Todos los campos (Nombre, Apellidos, DNI) son obligatorios.")
        return
    
    # Validar formato del DNI (ejemplo simple, se podría mejorar)
    if not (len(dni) >= 8 and dni[:-1].isdigit() and dni[-1].isalpha()): #Se añade una verificación del DNI.
      print("Error: El formato del DNI es incorrecto. Debe tener 8 números y una letra al final.")
      return

    # Si pasa las validaciones, se agrega el cliente
    nuevo_cliente = {'Nombre': nombre, 'Apellidos': apellidos, 'dni': dni}
    clientes.append(nuevo_cliente)
    print(f"Cliente {nombre} {apellidos} con DNI {dni} agregado correctamente.")


# Ejecutamos las funciones para probarlas
print("==LISTADO DE CLIENTES==")
print(clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111111A')  # Cliente existente
mostrar_cliente(clientes, '11111111Z')  # Cliente inexistente

print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222222V')  # Cliente inexistente
borrar_cliente(clientes, '22222222B')  # Cliente existente

print("\n==LISTADO DE CLIENTES==")
print(clientes)

print("\n==AGREGAR CLIENTES==")
agregar_cliente(clientes, "Ana", "Pérez", "33333333C")  # Cliente válido
agregar_cliente(clientes, "Luis", "García", "33333333C")  # DNI ya existe
agregar_cliente(clientes, "Maria", "", "44444444D")  # Apellidos vacíos
agregar_cliente(clientes, "Pedro", "López", "")  # DNI vacio
agregar_cliente(clientes, "", "Rodriguez", "55555555E") # Nombre Vacio
agregar_cliente(clientes, "Sandra", "Martinez", "123456789Z") # Dni con mas de 8 numeros.
agregar_cliente(clientes, "Carlos", "Sanchez", "ABCDEFGH") # Dni con letra al principio.

print("\n==LISTADO DE CLIENTES==")
print(clientes)