class Empleado:
    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre
        
    def set_cedula(self, cedula):
        self._cedula = cedula
        
    def get_cedula(self):
        return self._cedula
        
    def set_telefono(self, telefono):
        self._telefono = telefono
        
    def get_telefono(self):
        return self._telefono

class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, duracion_contrato):
        # constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)
        # Nuevos atributos
        self._nPlaza = nPlaza
        self._salarioBase = salarioBase
        self._duracion_contrato = duracion_contrato
    
    def set_nPlaza(self, nPlaza):
        self._nPlaza = nPlaza
    
    def get_nPlaza(self):
        return self._nPlaza
    
    def set_salarioBase(self, salarioBase):
        self._salarioBase = salarioBase
    
    def get_salarioBase(self):
        return self._salarioBase
    
    def set_duracion_contrato(self, duracion_contrato):
        self._duracion_contrato = duracion_contrato
    
    def get_duracion_contrato(self):
        return self._duracion_contrato
    
    # calcula el salario total
    def calcularSalarioTotal(self):
        return self._salarioBase + (self._salarioBase * 0.02)

class EmpleadoIndefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, categoria):
        # constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)
        # Nuevos atributos
        self._nPlaza = nPlaza
        self._salarioBase = salarioBase
        self._categoria = categoria
    
    def set_nPlaza(self, nPlaza):
        self._nPlaza = nPlaza
    
    def get_nPlaza(self):
        return self._nPlaza
    
    def set_salarioBase(self, salarioBase):
        self._salarioBase = salarioBase
    
    def get_salarioBase(self):
        return self._salarioBase
    
    def set_categoria(self, categoria):
        self._categoria = categoria
    
    def get_categoria(self):
        return self._categoria
    
    # calcula el salario total
    def calcularSalarioTotal(self):
        if self._categoria == 1:
            return self._salarioBase + (self._salarioBase * 0.03)
        elif self._categoria == 2:
            return self._salarioBase + (self._salarioBase * 0.05)
        elif self._categoria == 3:
            return self._salarioBase + (self._salarioBase * 0.08)
        else:
            return self._salarioBase

class EmpleadoSubcontratado(Empleado):
    def __init__(self, nombre, cedula, telefono, empresaResponsable):
        super().__init__(nombre, cedula, telefono)
        self._empresaResponsable = empresaResponsable

    def set_empresaResponsable(self, empresa):
        self._empresaResponsable = empresa

    def get_empresaResponsable(self):
        return self._empresaResponsable

# Empleados subcontratados
subContratado1 = EmpleadoSubcontratado("Roberto Flores Morales", 123456789, 88888888, "Coca-Cola")
subContratado2 = EmpleadoSubcontratado("Ana Mora Cruz", 223446789, 77777777, "Pepsi")

print("*** Empleados subcontratados ***")
print("\n****Empleado 1****")
print("Nombre: " + subContratado1.get_nombre() +
      "\nCédula: " + str(subContratado1.get_cedula()) +
      "\nTeléfono: " + str(subContratado1.get_telefono()) +
      "\nEmpresa responsable: " + subContratado1.get_empresaResponsable())

print("\n****Empleado 2****")
print("Nombre: " + subContratado2.get_nombre() +
      "\nCédula: " + str(subContratado2.get_cedula()) +
      "\nTeléfono: " + str(subContratado2.get_telefono()) +
      "\nEmpresa responsable: " + subContratado2.get_empresaResponsable())

# Empleados por tiempo definido
empleadoD = EmpleadoDefinido("Jeff Muñoz Castro", 345687324, 66666666, 3, 500000, 3)
empleadoD2 = EmpleadoDefinido("María Gonzáles Pérez", 983456783, 99999999, 6, 450000, 2)

print("\n*** Empleados de tiempo definido ***")
print("\n****Empleado 1****")
print("Nombre: " + empleadoD.get_nombre() +
      "\nCédula: " + str(empleadoD.get_cedula()) +
      "\nTeléfono: " + str(empleadoD.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoD.get_nPlaza()) +
      "\nDuracion contrato: " + str(empleadoD.get_duracion_contrato()) + " meses" +
      "\nSalario total: " + str(empleadoD.calcularSalarioTotal()))

print("\n****Empleado 2****")
print("Nombre: " + empleadoD2.get_nombre() +
      "\nCédula: " + str(empleadoD2.get_cedula()) +
      "\nTeléfono: " + str(empleadoD2.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoD2.get_nPlaza()) +
      "\nDuración contrato " + str(empleadoD2.get_duracion_contrato()) + " meses" +
      "\nSalario total: " + str(empleadoD2.calcularSalarioTotal()))

# Empleados por tiempo indefinido
empleadoI = EmpleadoIndefinido("Roberto Rojas Salazar", 434565432, 22222222, 4, 350000, 1)
empleadoI2 = EmpleadoIndefinido("Rebeca Suárez Tapia", 897456274, 33445533, 7, 510000, 2)
empleadoI3 = EmpleadoIndefinido("Sara Vega Montes", 989734567, 65786590, 19, 475000, 3)
empleadoI4 = EmpleadoIndefinido("Luis Sánchez Castillo", 546378763, 23546543, 23, 560000, 1)

print("\n*** Empleados de tiempo indefinido ***")
print("\n****Empleado 1****")
print("Nombre: " + empleadoI.get_nombre() +
      "\nCédula: " + str(empleadoI.get_cedula()) +
      "\nTeléfono: " + str(empleadoI.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoI.get_nPlaza()) +
      "\nCategoría: " + str(empleadoI.get_categoria()) +
      "\nSalario total: " + str(empleadoI.calcularSalarioTotal()))

print("\n****Empleado 2****")
print("Nombre: " + empleadoI2.get_nombre() +
      "\nCédula: " + str(empleadoI2.get_cedula()) +
      "\nTeléfono: " + str(empleadoI2.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoI2.get_nPlaza()) +
      "\nCategoría: " + str(empleadoI2.get_categoria()) +
      "\nSalario total: " + str(empleadoI2.calcularSalarioTotal()))

print("\n****Empleado 3****")
print("Nombre: " + empleadoI3.get_nombre() +
      "\nCédula: " + str(empleadoI3.get_cedula()) +
      "\nTeléfono: " + str(empleadoI3.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoI3.get_nPlaza()) +
      "\nCategoría: " + str(empleadoI3.get_categoria()) +
      "\nSalario total: " + str(empleadoI3.calcularSalarioTotal()))

print("\n****Empleado 4****")
print("Nombre: " + empleadoI4.get_nombre() +
      "\nCédula: " + str(empleadoI4.get_cedula()) +
      "\nTeléfono: " + str(empleadoI4.get_telefono()) +
      "\nNúmero de plaza: " + str(empleadoI4.get_nPlaza()) +
      "\nCategoría: " + str(empleadoI4.get_categoria()) +
      "\nSalario total: " + str(empleadoI4.calcularSalarioTotal()))