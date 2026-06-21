'''Metodos de string'''
# Los métodos son como una función que se encuentra dentro de un objeto.
asignatura = "Física cuántica"
print(asignatura.upper())
print(asignatura.lower())

ciencia = "Física del estado sólido"

print(ciencia.capitalize())

# Esto en css es capitalize.
print(ciencia.title())

ubicación1 = " lagos de Covadonga   asturias"
print(ubicación1.upper())
print(ubicación1.lower())
print(ubicación1.capitalize())
print(ubicación1.title())

ubicación2 = " cordillera del Himalaya   nepal   "
print(ubicación2.strip())
print(ubicación2.strip().capitalize())

ubicación3="   Sierra de Gredos     "
print(ubicación3.lstrip())
print(ubicación3.rstrip())
print(ubicación3.lstrip()+"Almanzor")
print(ubicación3.rstrip()+"Almanzor")

# Existe otro método que lo que hace es encontrar una cadena de caracteres dentro de nuestro string
#  y devolvernos el índice donde comienza.
# Hay que recordar que el índice empieza en 0
print(ubicación3.find("S"))
# Sensitive case
print(ubicación3.find("s"))
print(ubicación3.find("Sierra"))
print(ubicación3.find("sierra"))
print(ubicación3.find("Gr"))
print(ubicación3.lstrip().find("S"))
print(ubicación3.find("Física"))

# Reemplazar
print(ubicación3.replace("gredos", "Guadarrama"))
print(ubicación3.replace("Gredos", "Guadarrama"))
print(ubicación3)

# ubicación3 = ubicación3.replace("Gredos", "Guadarrama")
# print(ubicación3)
# print(ubicación3)
# print(ubicación3)

ubicación3_guion = ubicación3.strip().replace(" ", "_")
print(ubicación3_guion)

ubicación3_sin = ubicación3.replace(" ", "")
print(ubicación3_sin)

A = "Gredos"
B = "Guadarrama"
print(ubicación3.replace(A, B))
print(ubicación3)

print("de" in ubicación3)
# Es sensitive case 
print("De" in ubicación3)

A = "de"
print(A in ubicación3)

print("Cuántica" != ubicación3)
print("de" not in ubicación3)