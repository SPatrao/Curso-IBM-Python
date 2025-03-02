# Importamos todas las clases necesarias
from coche import Coche
from vehiculo import Vehiculo, Moto, Bicicleta
from persona import Persona, Empleado
from clientes import Cliente, Empresa


def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Trabajar con Coche")
        print("2. Trabajar con Vehículos")
        print("3. Trabajar con Personas")
        print("4. Trabajar con Clientes")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Opciones para Coche
            coche = Coche(color="azul")
            print(coche.estado())
            coche.arrancar()
            print(coche.estado())

        elif opcion == "2":
            # Opciones para Vehículos
            vehiculo = Vehiculo("Toyota", "Corolla")
            moto = Moto("Kawasaki", "Ninja")
            bicicleta = Bicicleta("azul", 2, "montaña")
            print(vehiculo.resumen())
            print(moto.resumen())
            print(bicicleta.resumen())

        elif opcion == "3":
            # Opciones para Personas
            persona = Persona("Juan", 30, "Madrid")
            empleado = Empleado(2000, 2020, "Manuel", 35, "Barcelona")
            print(persona.descripcion())
            print(empleado.descripcion())

        elif opcion == "4":
            # Opciones para Clientes
            cliente1 = Cliente("11111111A", "Hector", "Costa Guzman")
            cliente2 = Cliente("22222222B", "Juan", "Gonzalez Marquez")
            empresa = Empresa(clientes=[cliente1, cliente2])
            print("==LISTADO DE CLIENTES==")
            for cliente in empresa.clientes:
                print(cliente)
            empresa.mostrar_cliente("11111111A")
            empresa.borrar_cliente("22222222B")
            print("==LISTADO DE CLIENTES==")
            for cliente in empresa.clientes:
                print(cliente)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()