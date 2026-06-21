'''Más de bucles o loop for'''
contraseña = '1234'

for n in range (3):
    print("Intento:", n+1)
    tucontraseña = input("Introduce la contraseña a ver si aciertas: ")
    if tucontraseña == contraseña:
        print("Has acertado:", contraseña, "en el intento", n+1)
        break
else:
    print("No has acertado, has agotado todos los intentos")
