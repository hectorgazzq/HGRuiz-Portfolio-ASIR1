'''Iterables con Loop for'''

for n in "Administración de sistemas informáticos en red":
    print(n)

for caracter in "Administración de sistemas informáticos en red":
    print(caracter)

with open("iterables.txt", "a") as fichero:
    for caracter in "Programación con Python":
        fichero.write(f'{caracter}\n')

