'''Números en Python'''
edad = "18" # edad entero o integer
print(edad)
nota = 8.9 # nota decimal o float
print(nota)

complejo = 5+3j
print(complejo)

sumando1 = 7
sumando2 = 3
suma = sumando1 + sumando2
print("La suma de", sumando1, "+", sumando2, "es:", suma)

resto1 = 70
resto2 = 30
resta = resto1 - resto2
print("La resta de", resto1, "-", resto2, "es:", resta)

multiplo1 = 5
multiplo2 = 15
producto = multiplo1 * multiplo2
print("El producto de", multiplo1, "x", multiplo2, "es:", producto)

dividendo1 = 80
dividendo2 = 3
división = dividendo1 / dividendo2
print("La división de", dividendo1, "/", dividendo2, "es:", división)

# División entera, muestra la parte entera de la dividendo>divisor
dividendo = 7
divisor = 3
división_entera = dividendo / divisor
print("La división entera de", dividendo,
       "entre", divisor, "es:", división_entera)

# Resto  o módulo, muestra el resto de la división sin sacar decimales dividendo<divisor
dividendo = 7
divisor = 3
modulo = dividendo % divisor
print("El resto de la división entera sin sacar decimales de", dividendo,
       "modulo", divisor, "es:", división_entera)

# Potencias
base = 2
exponente = 3
potencia = base**exponente
print("La potencia de", base,
       "elevado", exponente, "es:", potencia)

# Algunos atajos en operaciones, forma larga

print("contador, aumento de 1")
contador = 8
print(contador)
contador = contador + 1
print(contador)

print("Forma corta de operación, del contador anterior")
contador = 8
print(contador)
contador += 1
print(contador)

# También vale para el resto de operaciones
print("Forma corta con suma")
# Suma
a = 14
print(a)
a += 2
print(a)

print("Forma corta con resta")
# Resta
a = 14
print(a)
a -= 2
print(a)

print("Forma corta con producto")
# Producto
a = 14
print(a)
a *= 2
print(a)

print("Forma corta con división")
# División
a = 14
print(a)
a //= 2
print(a)

print("Forma corta con potencia")
# Potencia
a = 14
print(a)
a **= 2
print(a)

print("Forma corta con división entera")
# División entera
a = 25
print(a)
a //= 2
print(a)

print("Forma corta con módulo")
# Módulo
a = 25
print(a)
a %= 2
print(a)


a = 14
a += 2
a -= 2
a *= 2
a /= 2
a **= 2
a //= 2
a %= 2
print(a)