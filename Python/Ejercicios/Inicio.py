Saludo ="Hola Mundo"
saludo ='hola mundo'
print(Saludo)
print(saludo)

def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b
a, b = 5, 10
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función
print()
def minimo(l):
    l[0] = 1000 # Modificamos la lista en el interior
    return min(l)

l = [1, 2, 3]
print(l)

print(minimo(l)) # Modifica la lista aquí

print(l)

