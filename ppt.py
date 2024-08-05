ganadas_jugador1 = 0
ganadas_jugador2 = 0

intentos = 0
intentos_max = 3

nombre1= input("¿Como se llamara el jugador 1?: ")
nombre2= input("¿Como se llamara el jugador 2?: ")
jugador1 = input("Hola " + nombre1 + " Que eliges? Piedra, papel o tijeras?: ").lower()
jugador2 = input("Hola " + nombre2 + " Que eliges? Piedra, papel o tijeras?: ").lower()
if jugador1 == jugador2:
    print("Ha sido un empate")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra" ) or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("Ha ganado: ", nombre1)
    ganadas_jugador1 += 1
else:
    print("Ha ganado: ", nombre2)
    ganadas_jugador2 += 1
intentos += 1

while intentos < intentos_max:
    jugador1 = input(nombre1 + " Que eliges? Piedra, papel o tijeras?: ").lower()
    jugador2 = input(nombre2 + " Que eliges? Piedra, papel o tijeras?: ").lower()
    if jugador1 == jugador2:
        print("Ha sido un empate")
    elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra" ) or (jugador1 == "tijeras" and jugador2 == "papel"):
        print("Ha ganado: ", nombre1)
        ganadas_jugador1 += 1
    else:
        print("Ha ganado: ", nombre2)
        ganadas_jugador2 += 1
    intentos += 1

if ganadas_jugador1 == ganadas_jugador2:
    print("Terminó el juego. Fue empate")
elif ganadas_jugador1 > ganadas_jugador2:
    print("Terminó el juego, ganó: " + nombre1 )
else:
    print("Terminó el juego, ganó: " + nombre2 )

