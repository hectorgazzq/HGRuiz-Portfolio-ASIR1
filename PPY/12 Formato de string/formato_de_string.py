'''Formato de variables tipo string'''
nombre = "Héctor"
Apellido = "Gázquez"
Apellido2 = "Ruiz"

# Vamos a concatenar (unir) strings usando el operador +
# que si está rodeado de strings, los concatena

nombre_completo = nombre+Apellido+Apellido2
print(nombre_completo)

nombre_completo = nombre+" "+Apellido+" "+Apellido2
print(nombre_completo)

# Se usa f "{}espacio en blanco" format()

nivel = "Fundamentos de"
tipo = "Programación"
lenguaje = "Python"
nombre_modulo = f"{nivel} {tipo} {lenguaje}"
print(nombre_modulo)

# Conseguir el siguiente texto GBD = 6 horas por semana
módulo = "Gestión de Bases de Datos"
dia1 = 1
dia2 = 2
dia3 = 3
datos_módulo = f"{módulo[0]}{módulo[11]}{módulo[20]} {"="} {dia1+dia2+dia3} {"horas por semana"}"

print(datos_módulo)
