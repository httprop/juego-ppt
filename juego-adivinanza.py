import random


numero_secreto = random.randint(1,101)
adivinado = False
cant_intentos = 0
cant_max_intentos = 10
print("Bienvenido al juego de adivinar el número secreto")
while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Introduce un número del 1 al 100: ") 
    numero = int(entrada)
    if numero == numero_secreto:
        print("Felicidades, adivinaste el número secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El numero es menor al ingresado") 
    cant_intentos += 1 
if not cant_intentos < cant_max_intentos:
    print("Game over. No pudiste adivinar dentro de los 10 intentos")