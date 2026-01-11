#Este es el archivo de la tragaperras

import random
import time


def simbolos():
    simbolos = ["🍒", "🍊", "🍉", "🍇", "🔔", "💎", "⭐", "🍀"]
    return simbolos

def eleccion_tragaperras(simbolos_juego):
    eleccion_maquina=random.choices(simbolos_juego,k=3)
    return eleccion_maquina
        


def main_tragaperras(saldo_total):
    print("""
    ******************************
    *                            *
    *    🎰  T R A G A P E R R A S   🎰    *
    *                            *
    ******************************
    """)

    simbolos_juego=simbolos()
    
    while True:
        print("Tu Saldo: ",saldo_total)
        tecla = input("Presiona [E] para tirar o [Q] para salir: ")
        if saldo_total<=0:
            print("Ya no tienes saldo , saliendo al menu principal...")
            time.sleep(2)
        else:
            if tecla=="e":
                eleccion_juego=eleccion_tragaperras(simbolos_juego)
                saldo_total-=1
                print(eleccion_juego)
                if eleccion_juego[0]==eleccion_juego[1]==eleccion_juego[2]:
                    print("Has Ganado x50!!")
                    saldo_total+=50
                elif eleccion_juego[0]==eleccion_juego[1] or eleccion_juego[1]==eleccion_juego[2]:
                    print("Has ganado x25!!")
                    saldo_total+=25
                else:
                    saldo_total-=1
            elif tecla=="q":
                print("Saliendo...")
                time.sleep(2)
                break
            else:
                print("Tecla invalida")
                continue
    return saldo_total


    
