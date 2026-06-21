'''If notas'''
nota = float(input("Introduce la nota:"))
print(nota)
mensaje = "nada"
if nota > 10:
    mensaje = "Nota fuera de rango"
elif nota == 10:
    mensaje = "Matrícula de honor"
elif nota >= 9:
    mensaje = "Sobresaliente"
elif nota >= 7:
    mensaje = "Notable"
elif nota >= 6:
    mensaje = "Bien"
elif nota >= 5:
    mensaje = "Aprobado"
elif nota >= 0:
    mensaje = "Suspenso"
else:
    mensaje = "No es una nota" # para números negativos
print(mensaje)
