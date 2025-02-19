import tkinter as tk  # Importamos la biblioteca Tkinter para crear la interfaz gráfica
from tkinter import ttk  # Importamos ttk para utilizar widgets más modernos

# Función que realiza la operación matemática según la selección del usuario
def calcular():
    try:
        # Obtenemos los valores ingresados en los campos de entrada
        num1 = float(entry1.get())  # Convertimos el primer número a flotante
        num2 = float(entry2.get())  # Convertimos el segundo número a flotante
        operacion = combo.get()  # Obtenemos la operación seleccionada en el combobox

        # Realizamos la operación matemática seleccionada
        if operacion == "Suma":
            resultado.set(num1 + num2)  # Suma los números y actualiza el resultado
        elif operacion == "Resta":
            resultado.set(num1 - num2)  # Resta los números y actualiza el resultado
        elif operacion == "Multiplicación":
            resultado.set(num1 * num2)  # Multiplica los números y actualiza el resultado
        elif operacion == "División":
            if num2 != 0:
                resultado.set(num1 / num2)  # Realiza la división si el divisor no es 0
            else:
                resultado.set("Error: División por 0")  # Manejo de error si el divisor es 0
    except ValueError:
        resultado.set("Error: Entrada inválida")  # Manejo de error si la entrada no es válida

# Crear la ventana principal
root = tk.Tk()  # Inicializamos la ventana principal de Tkinter
root.title("Calculadora")  # Asignamos un título a la ventana

# Variable que almacenará el resultado de la operación
resultado = tk.StringVar()  # StringVar permite actualizar dinámicamente el contenido

# Creación de los widgets de la interfaz gráfica
# Etiqueta y campo de entrada para el primer número
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)  # Campo de entrada para el primer número
entry1.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de entrada para el segundo número
tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)  # Campo de entrada para el segundo número
entry2.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta y combobox para seleccionar la operación matemática
tk.Label(root, text="Operación:").grid(row=2, column=0, padx=5, pady=5)
combo = ttk.Combobox(root, values=["Suma", "Resta", "Multiplicación", "División"])  # Menú desplegable con opciones
combo.grid(row=2, column=1, padx=5, pady=5)
combo.current(0)  # Establecemos "Suma" como la opción seleccionada por defecto

# Botón para ejecutar el cálculo
tk.Button(root, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta y campo para mostrar el resultado de la operación
tk.Label(root, text="Resultado:").grid(row=4, column=0, padx=5, pady=5)
tk.Label(root, textvariable=resultado).grid(row=4, column=1, padx=5, pady=5)

# Inicia el bucle principal de la aplicación
root.mainloop()  # Muestra la ventana y mantiene la aplicación en ejecución
