'''Calculadora básica'''
# input() toma lo que recoge del usuario como string
a1 = input("Introduce el primer número:")
a2 = input("Introduce el segundo número:")
a = a1+a2
print(a)

#Solucionamos
a1 = input("Introduce el primer número:")
a1 = int(a1)

#Otra manera
a2 = int(input("Introduce el segundo número:"))

a = a1+a2
print(a)
##############################################################
a1 = int(input("Introduce el primer número:"))
a2 = int(input("Introduce el segundo número:"))
suma = a1+a2
resta = a1-a2
multiplicación = a1*a2
división = a1/a2

mensaje1 = f"Con los números introducidos, {a1} {a2}, la suma es {suma}, la resta es {resta}, la multiplicación es {multiplicación}, y la división es {división}"
print(mensaje1)

# print(suma)
# print(resta)
# print(multiplicación)
# print(división)

mensaje2 = f"""
Con los números introducidos {a1} y {a2}
la suma es {suma}
la resta es {resta}
la multiplicación es {multiplicación}
y la división es {división}
"""
print(mensaje2)
