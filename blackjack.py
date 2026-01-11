import random
import time

def cartas():
    return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

valores = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def eleccion_maquina(mazo):
    lista_maquina = []
    suma_total = 0
    estado_maquina = True
    while suma_total < 17:
        carta = random.choice(mazo)
        lista_maquina.append(carta)
        if carta == 'A' and suma_total + 11 > 21:
            suma_total += 1
        else:
            suma_total += valores[carta]
    if suma_total > 21:
        print("La máquina ha perdido, su valor total es {}".format(suma_total))
        estado_maquina = False
    return suma_total, lista_maquina, estado_maquina

def eleccion_jugador(mazo):
    lista_jugador = []
    suma_jugador = 0
    estado_jugador = True
    while True:
        eleccion = input("[E]SACAR CARTA / [Q] PLANTARSE: ").lower()
        if eleccion in ["e", "q"]:
            break
        print("Tecla incorrecta, inténtalo de nuevo...")

    while suma_jugador < 21 and eleccion == "e":
        carta = random.choice(mazo)
        lista_jugador.append(carta)
        if carta == 'A' and suma_jugador + 11 > 21:
            suma_jugador += 1
        else:
            suma_jugador += valores[carta]

        print("Has sacado: {}, Total: {}".format(carta, suma_jugador))

        if suma_jugador >= 21:
            break

        eleccion = input("[E]SACAR CARTA / [Q] PLANTARSE: ").lower()
        while eleccion not in ["e", "q"]:
            print("Letra incorrecta, inténtalo de nuevo.")
            continue

    if suma_jugador > 21:
        print("Has perdido, has superado el 21. Tu valor total es {}".format(suma_jugador))
        estado_jugador = False
    else:
        print("Tus cartas: {} → Total: {}".format(lista_jugador, suma_jugador))

    return suma_jugador, lista_jugador, estado_jugador

def main_blackjack(saldo_total):
    print("""
    ******************************
    *                            *
    *     🂡  B L A C K J A C K  🂡     *
    *                            *
    ******************************
    """)

    print("Bienvenido a la zona del blackjack!! Gracias por estar con Casinos Jaume")
    seguir = True
    print("Tu saldo: ", saldo_total)

    while seguir and saldo_total > 0:
        try:
            saldo_jugada = int(input("¿Qué cantidad quieres apostar en esta jugada? "))
        except ValueError:
            print("Cantidad inválida.")
            continue

        if saldo_jugada > saldo_total or saldo_jugada <= 0:
            print("No puedes apostar más de tu saldo o una cantidad no válida.")
            continue

        saldo_total -= saldo_jugada
        mazo = cartas()
        suma_total, lista_maquina, estado_maquina = eleccion_maquina(mazo)
        suma_jugador, lista_jugador, estado_jugador = eleccion_jugador(mazo)

        if not estado_jugador:
            print("La máquina ha ganado.Con {} y Total {}".format(lista_maquina,suma_total))
        elif not estado_maquina:
            print("El jugador ha ganado.")
            print("Cartas Maquina - {} Total {}".format(lista_maquina,suma_total))
            saldo_total += saldo_jugada * 2
        elif suma_jugador == suma_total or suma_total==suma_jugador:
            print("EMPATE!!")
            print("Cartas Maquina -- {} Total {}".format(lista_maquina,suma_total))
        elif suma_jugador > suma_total:
            print("¡Has ganado esta ronda!")
            print("Cartas jugador - {} Total {}".format(lista_jugador,lista_maquina))
            saldo_total += saldo_jugada * 2
        else:
            print("Lo siento, has perdido.")
            print("Tu rival tenía: {} -- Total ({})".format(lista_maquina, suma_total))

        print("Tu saldo actual: {}".format(saldo_total))
        if saldo_total <= 0:
            print("Te has quedado sin saldo.")
            break

        eleccion_salida = input("¿Deseas salir o continuar? [E] CONTINUAR / [Q] SALIR: ").lower()
        if eleccion_salida == "q":
            seguir = False
        else:
            print("Barajando las cartas...")
            time.sleep(2)

    return saldo_total


    




