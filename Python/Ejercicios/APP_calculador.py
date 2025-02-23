import tkinter as tk
from tkinter import ttk

# Función que realiza el cálculo según la operación seleccionada
def calcular():
    try:
        # Se obtienen los valores de los campos de entrada y se convierten a float
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = operacion_seleccionada.get()
        
        # Se evalúa qué operación realizar y se actualiza el resultado
        if operacion == "Suma":
            resultado.set(num1 + num2)
        elif operacion == "Resta":
            resultado.set(num1 - num2)
        elif operacion == "Multiplicación":
            resultado.set(num1 * num2)
        elif operacion == "División":
            if num2 != 0:
                resultado.set(num1 / num2)
            else:
                resultado.set("Error: Div entre 0")  # Control de error para la división por cero
    except ValueError:
        resultado.set("Entrada no válida")  # Manejo de error si los valores no son numéricos

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")  # Título de la ventana

# Creación de widgets
# Campo de entrada para el primer número
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Campo de entrada para el segundo número
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Lista de operaciones disponibles en un combobox
tk.Label(root, text="Seleccione una operación:").pack(pady=2)
operaciones = ["Suma", "Resta", "Multiplicación", "División"]
operacion_seleccionada = tk.StringVar(value=operaciones[0])  # Se selecciona "Suma" por defecto
combo_operaciones = ttk.Combobox(root, values=operaciones, textvariable=operacion_seleccionada)
combo_operaciones.pack(pady=5)

# Botón para ejecutar el cálculo
btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.pack(pady=5)

# Etiqueta para mostrar el resultado
resultado = tk.StringVar()  # Variable que almacena el resultado
label_resultado = tk.Label(root, textvariable=resultado)
label_resultado.pack(pady=5)

# Inicia el bucle principal de la aplicación para mostrar la interfaz
root.mainloop()