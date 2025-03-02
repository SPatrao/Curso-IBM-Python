#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

# Definimos una lista de clientes, donde cada cliente es un diccionario con Nombre, Apellidos y DNI
clientes = [
    {'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'},
    {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}
]

def mostrar_cliente(clientes):
    """
    Muestra la información de un cliente a partir de su DNI, pidiéndolo por teclado.

    Args:
        clientes (list): La lista de clientes.
    """
    dni = input("Introduce el DNI del cliente a mostrar: ")
    for c in clientes:
        if dni == c['dni']:
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            return
    logging.error("Cliente no encontrado")
    print(f"Cliente con ID {dni} no encontrado")

def borrar_cliente(clientes):
    """
    Borra un cliente de la lista a partir de su DNI, pidiéndolo por teclado.

    Args:
        clientes (list): La lista de clientes.
    """
    dni = input("Introduce el DNI del cliente a borrar: ")
    for i, c in enumerate(clientes):
        if dni == c['dni']:
            del clientes[i]
            print(str(c), "> BORRADO")
            return
    logging.error("Cliente no encontrado")
    print(f"Cliente con ID {dni} no encontrado")

def agregar_cliente(clientes):
    """
    Agrega un nuevo cliente a la lista, pidiendo los datos por teclado.

    Args:
        clientes (list): La lista de clientes.
    """
    nombre = input("Nombre del cliente: ")
    apellidos = input("Apellidos del cliente: ")
    dni = input("DNI del cliente: ")

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
    if not (len(dni) >= 8 and dni[:-1].isdigit() and dni[-1].isalpha()):
        print("Error: El formato del DNI es incorrecto. Debe tener 8 números y una letra al final.")
        return

    # Si pasa las validaciones, se agrega el cliente
    nuevo_cliente = {'Nombre': nombre, 'Apellidos': apellidos, 'dni': dni}
    clientes.append(nuevo_cliente)
    print(f"Cliente {nombre} {apellidos} con DNI {dni} agregado correctamente.")

def mostrar_todos_clientes(clientes):
    """
    Muestra la lista de todos los clientes.

    Args:
        clientes (list): La lista de clientes.
    """
    print("==LISTADO DE CLIENTES==")
    for cliente in clientes:
        print(cliente)

def main():
    """
    Función principal que muestra el menú y gestiona las opciones del usuario.
    """
    # Añadimos clientes iniciales
    clientes.append({'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'})
    clientes.append({'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'})
    while True:
        print("\n==== MENÚ ====")
        print("1. Agregar cliente")
        print("2. Mostrar cliente por DNI")
        print("3. Borrar cliente por DNI")
        print("4. Mostrar todos los clientes")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_cliente(clientes)
        elif opcion == '2':
            mostrar_cliente(clientes)
        elif opcion == '3':
            borrar_cliente(clientes)
        elif opcion == '4':
            mostrar_todos_clientes(clientes)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")


if __name__ == "__main__":
    main()
