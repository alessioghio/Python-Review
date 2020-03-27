from myFunctions import expo
import myFunctions

# Print
# print(-3)
# print("hola vomo estas")

# Variables
a = 80
nombre = "bruno"
apellido = "belevan"
#print(a)
a = 10
#print(a)

# Type of variables
#   string
#       s.capitalize(), s.upper(), s.lower(), s.replace(a, b), s.split()
# print(nombre.capitalize())
# print(nombre.upper())
# print(nombre.replace('o','e'))
oracion = "bruno es mi amigo"
# print(oracion.split())
nombre2 = nombre.capitalize()
# print(nombre2)

a = 80 # int
gravedad = 9.81 # float o double SON PARA NUMEROS DECIMALES
boolean = True # 1 o 0
nombre = "bruno" # string

# print(type(gravedad))
# print(type(nombre))
# print(type(boolean))

# Operators
# sum: +
# subtract: -
# division: /
# multiplication: *
# power: ** IMPORTANTE

#print(nombre + " " + apellido)
#print("La gravedad es: " + str(gravedad) + " m/s^2")
#print("La gravedad es:", gravedad, "m/s^2")
#print("La gravedad es: %.3f m/s^2" % (gravedad))
#print("La gravedad es %f y %s lo sabe" % (gravedad,nombre))

# Functions and imports
def sumar2nums(num1, num2):
    res = num1 + num2
    return res

resultado = sumar2nums(5,3)

exponencial = expo(2,3)
print(exponencial)

myFunctions.welcomeMSG()

# Conditions
#   if, elif, else

# Loops
#   for, while
#       in range()

# Pointers

# Lists
#   copy function
#   append, pop

# Slicing

# Enumerate and double iterators in for loops

# Dictionaries
# d.items()

# Tuples

# Sets
# s.add(), s.remove()

# Classes
#   Constructor
#       def __init__(self, variable=0):
#           self.value = variable
#   Methods
 