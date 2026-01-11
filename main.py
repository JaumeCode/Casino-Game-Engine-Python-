#Programa principal de casino
import time
from ruleta import main_ruleta
from tragaperras import main_tragaperras
from blackjack import main_blackjack

def main():
    while True:
        print("""
            ********************************************
            *                                          *
            *         ✦ CASINOS JAUME ✦               *
            *                                          *
            ********************************************
        """)
        print("Bienvenidos a casinos jaume,gracias por elegirnos a nostros...")
        time.sleep(2)
        saldo_total=int(input("Que cantidad de saldo quieres meter?"))
        print("Estos son nuestros juegos disponibles--")
        print("1-Ruleta")
        print("2-Blackjack")
        print("3-Tragaperras")
        eleccion_menu=input("Que juego quieres escojer?")
        if eleccion_menu == "1":
            main_ruleta(saldo_total)
        elif eleccion_menu == "2":
            main_blackjack(saldo_total)
        elif eleccion_menu == "3":
            main_tragaperras(saldo_total)
        else:
            comprobacion=input("Error al seleccionar modalidad , deseas salir? [Q] SI / [E] NO")
            if comprobacion == "si":
                break
            else:
                continue
    print("Gracias por Venir a Casinos Jaume a pasar una gran velada")
    

main()

