'''Importando el módulo Math'''
# Importar una librería
import math 

# math.ceil() redondea al número entero más cercanopor arriba
print("Probando math.ceil()")
print(math.ceil(3.43))
print(math.ceil(-3.43))

a = 5
b = 2
print(a/b)
print(math.ceil(a/b))
print(round(a/b))

# math.floor() redondea al número entero más cercano por abajo
print("Probando math.floor()")
print(math.floor(3.99))
print(math.floor(-3.99))


# math.isnan() "isnan" sgnifica "no es un número" por tanto devuelve false si es número
print("Probando math.isnan()")
print(math.isnan(56.24))
#print(math.isnan("56.24")) #ERROR

# math.pow(base, exponente) es hacer potencias
print("Probando math.pow()")
print(math.pow(2, 8))
 
# math.sqrt() raíz cuadrada
print("Probando math.sqrt()")
print(math.sqrt(144))
