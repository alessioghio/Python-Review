from myFunctions import expo
# import myFunctions
import myFunctions as mf

C2F = mf.C2F

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
# % modulus

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
# print(exponencial)

# mf.welcomeMSG()
# print(C2F(0))

# Conditions
#   if, elif, else
# Boolean <--- important
# == : compare identical values
# < and <=
# > and >=
# !=
# or : logic OR
# and logic AND
input = "sdgesaer"
condition = input == nombre # THIS IS BOOLEAN
# print(condition)

"""
if(condition):
    print("somos tocayos")
elif(input == "alessio"):
    print("eres uno de mis mejores amigos")
else:
    print("igual podemos ser amigos")
"""
"""
bankAccount = 0
if(bankAccount > 0):
    print("tenemos dinero")
elif(bankAccount == 0):
    print("Estamos en la bancarrota")
else:
    print("el cagadon debemos plata")
"""

# Loops
#   for -> in range() # when you the number of iterations
#   while # when you don't know th enumber of iterations

"""
# Prime number finder
for i in range(1,101):
    count = 0
    if(i==1 or i==2):
        print("Number %d is prime" % (i))
        continue # break
    for j in range(i-1,1,-1):
        if(i%j==0):
            count = count + 1
    if(count==0):
        print("Number %d is prime" % (i))
"""
"""
input = 101
print(input)
while(input!=1):
    if(input%2==0):
        input /= 2
        print(input)
    else:
        input = 3*input + 1
        print(input)
"""

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
 