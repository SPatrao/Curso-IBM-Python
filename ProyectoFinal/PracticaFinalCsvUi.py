import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo  
        self.autor = autor  
        self.isbn = isbn  
        self.disponible = True  

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True, f'Libro "{self.titulo}" prestado con éxito.'
        else:
            return False, f'El libro "{self.titulo}" ya está prestado.'

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True, f'Libro "{self.titulo}" devuelto con éxito.'
        else:
            return False, f'El libro "{self.titulo}" ya estaba disponible.'

    def mostrar(self):
        estado = 'Sí' if self.disponible else 'No'
        return f'- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}'
    
    def buscar(self):
        estado = 'Disponible' if self.disponible else 'No disponible'
        return f'{self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Estado: {estado}'

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.isbn_counter = 100000000  

    def generar_isbn_continuo(self):
        while str(self.isbn_counter) in self.libros:
            self.isbn_counter += 1  
        return str(self.isbn_counter)

    def validar_isbn(self, isbn):
        return isbn.isdigit() and len(isbn) == 9

    def agregar_libro(self, titulo, autor, isbn=None):
        if not isbn:
            isbn = self.generar_isbn_continuo()
            mensaje = f"ISBN generado automáticamente: {isbn}"
        elif not self.validar_isbn(isbn):
            return False, "El ISBN debe ser un número de 9 dígitos."
        
        if isbn in self.libros:
            return False, f"El libro con ISBN {isbn} ya está en la biblioteca."

        libro = Libro(titulo, autor, isbn)
        self.libros[isbn] = libro
        return True, f'Libro "{titulo}" agregado con éxito (ISBN: {isbn}).'

    def prestar_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            return libro.prestar()
        else:
            return False, f"Error: No se encontró un libro con ISBN {isbn}."

    def devolver_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            return libro.devolver()
        else:
            return False, f"Error: No se encontró un libro con ISBN {isbn}."

    def buscar_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro:
            return True, libro.buscar()
        else:
            return False, "Libro no encontrado."

    def obtener_todos_libros(self):
        return list(self.libros.values())

    def cargar_libros_csv(self, archivo_csv):
        try:
            with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
                lector_csv = csv.DictReader(archivo)
                libros_agregados = 0
                
                for fila in lector_csv:
                    titulo = fila.get('Title', '').strip()
                    autor = fila.get('Author', 'Desconocido').strip()
                    if titulo:
                        self.agregar_libro(titulo, autor)
                        libros_agregados += 1

            return True, f"Carga completada. Se agregaron {libros_agregados} libros."
        except FileNotFoundError:
            return False, f"Error: No se encontró el archivo {archivo_csv}."
        except Exception as e:
            return False, f"Error al cargar el archivo CSV: {e}"

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")
        self.root.geometry("800x600")
        self.root.configure(padx=10, pady=10)
        
        self.biblioteca = Biblioteca()
        
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_var.set("Bienvenido al Sistema de Gestión de Biblioteca")
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        self.tab_gestion = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_gestion, text="Gestión de Libros")
        
        self.tab_visualizacion = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_visualizacion, text="Visualización de Libros")
        
        self.setup_gestion_tab()
        
        self.setup_visualizacion_tab()

    def validar_isbn_input(self, isbn):
        """Valida que el ISBN sea un número de 9 dígitos"""
        if not isbn:
            return True, ""
        
        if not isbn.isdigit():
            return False, "El ISBN debe contener solo dígitos numéricos."
        
        if len(isbn) != 9:
            return False, f"El ISBN debe tener exactamente 9 dígitos (actual: {len(isbn)})."
            
        return True, ""

    def setup_gestion_tab(self):
        agregar_frame = ttk.LabelFrame(self.tab_gestion, text="Agregar Libro")
        agregar_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(agregar_frame, text="Título:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.titulo_var = tk.StringVar()
        ttk.Entry(agregar_frame, textvariable=self.titulo_var, width=40).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(agregar_frame, text="Autor:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.autor_var = tk.StringVar()
        ttk.Entry(agregar_frame, textvariable=self.autor_var, width=40).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(agregar_frame, text="ISBN (9 dígitos):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.isbn_var = tk.StringVar()
        self.isbn_entry = ttk.Entry(agregar_frame, textvariable=self.isbn_var, width=40)
        self.isbn_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.isbn_info_var = tk.StringVar()
        self.isbn_info_label = ttk.Label(agregar_frame, textvariable=self.isbn_info_var, foreground="gray")
        self.isbn_info_label.grid(row=3, column=1, padx=5, pady=0, sticky=tk.W)
        self.isbn_info_var.set("Dejar en blanco para generar automáticamente")
        
        ttk.Button(agregar_frame, text="Agregar Libro", command=self.agregar_libro).grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        
        prestamo_frame = ttk.LabelFrame(self.tab_gestion, text="Préstamos y Devoluciones")
        prestamo_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(prestamo_frame, text="ISBN (9 dígitos):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.prestamo_isbn_var = tk.StringVar()
        self.prestamo_isbn_entry = ttk.Entry(prestamo_frame, textvariable=self.prestamo_isbn_var, width=20)
        self.prestamo_isbn_entry.grid(row=0, column=1, padx=5, pady=5)
        
        button_frame = ttk.Frame(prestamo_frame)
        button_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Prestar", command=self.prestar_libro).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Devolver", command=self.devolver_libro).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Buscar", command=self.buscar_libro).pack(side=tk.LEFT, padx=5)
        
        csv_frame = ttk.LabelFrame(self.tab_gestion, text="Cargar desde CSV")
        csv_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(csv_frame, text="Seleccionar archivo CSV", command=self.cargar_csv).pack(padx=5, pady=10)

    def setup_visualizacion_tab(self):
        table_frame = ttk.Frame(self.tab_visualizacion)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        columns = ("titulo", "autor", "isbn", "disponible")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        self.tree.heading("titulo", text="Título")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("isbn", text="ISBN")
        self.tree.heading("disponible", text="Disponible")
        
        self.tree.column("titulo", width=250)
        self.tree.column("autor", width=150)
        self.tree.column("isbn", width=100)
        self.tree.column("disponible", width=80)
        
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        
        ttk.Button(self.tab_visualizacion, text="Actualizar Lista", command=self.actualizar_lista).pack(padx=10, pady=10)
        
        self.actualizar_lista()

    def agregar_libro(self):
        titulo = self.titulo_var.get().strip()
        autor = self.autor_var.get().strip()
        isbn = self.isbn_var.get().strip()
        
        if not titulo:
            messagebox.showerror("Error", "El título es obligatorio")
            return
            
        if not autor:
            autor = "Desconocido"
        
        if isbn:
            is_valid, error_msg = self.validar_isbn_input(isbn)
            if not is_valid:
                messagebox.showerror("Error de ISBN", error_msg)
                self.isbn_entry.focus()
                return
        
        if not isbn:
            resultado, mensaje = self.biblioteca.agregar_libro(titulo, autor)
        else:
            resultado, mensaje = self.biblioteca.agregar_libro(titulo, autor, isbn)
        
        if resultado:
            messagebox.showinfo("Éxito", mensaje)
            self.titulo_var.set("")
            self.autor_var.set("")
            self.isbn_var.set("")
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", mensaje)
        
        self.status_var.set(mensaje)

    def prestar_libro(self):
        isbn = self.prestamo_isbn_var.get().strip()
        if not isbn:
            messagebox.showerror("Error", "Ingrese un ISBN")
            self.prestamo_isbn_entry.focus()
            return
            
        is_valid, error_msg = self.validar_isbn_input(isbn)
        if not is_valid:
            messagebox.showerror("Error de ISBN", error_msg)
            self.prestamo_isbn_entry.focus()
            return
            
        resultado, mensaje = self.biblioteca.prestar_libro(isbn)
        
        if resultado:
            messagebox.showinfo("Préstamo", mensaje)
            self.prestamo_isbn_var.set("")  
        else:
            messagebox.showerror("Error", mensaje)
            
        self.status_var.set(mensaje)
        self.actualizar_lista()

    def devolver_libro(self):
        isbn = self.prestamo_isbn_var.get().strip()
        if not isbn:
            messagebox.showerror("Error", "Ingrese un ISBN")
            self.prestamo_isbn_entry.focus()
            return
            
        is_valid, error_msg = self.validar_isbn_input(isbn)
        if not is_valid:
            messagebox.showerror("Error de ISBN", error_msg)
            self.prestamo_isbn_entry.focus()
            return
            
        resultado, mensaje = self.biblioteca.devolver_libro(isbn)
        
        if resultado:
            messagebox.showinfo("Devolución", mensaje)
            self.prestamo_isbn_var.set("")
        else:
            messagebox.showerror("Error", mensaje)
            
        self.status_var.set(mensaje)
        self.actualizar_lista()

    def buscar_libro(self):
        isbn = self.prestamo_isbn_var.get().strip()
        if not isbn:
            messagebox.showerror("Error", "Ingrese un ISBN")
            self.prestamo_isbn_entry.focus()
            return
            
        is_valid, error_msg = self.validar_isbn_input(isbn)
        if not is_valid:
            messagebox.showerror("Error de ISBN", error_msg)
            self.prestamo_isbn_entry.focus()
            return
            
        resultado, mensaje = self.biblioteca.buscar_libro(isbn)
        
        if resultado:
            messagebox.showinfo("Información del Libro", mensaje)
        else:
            messagebox.showerror("Error", mensaje)
            
        self.status_var.set(mensaje)

    def cargar_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if not filename:
            return
            
        resultado, mensaje = self.biblioteca.cargar_libros_csv(filename)
        
        if resultado:
            messagebox.showinfo("Carga CSV", mensaje)
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", mensaje)
            
        self.status_var.set(mensaje)

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        libros = self.biblioteca.obtener_todos_libros()
        
        for libro in libros:
            estado = "Sí" if libro.disponible else "No"
            self.tree.insert("", tk.END, values=(libro.titulo, libro.autor, libro.isbn, estado))
            
        self.status_var.set(f"Mostrando {len(libros)} libros")

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()