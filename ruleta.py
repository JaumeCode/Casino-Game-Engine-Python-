#Este es el archivo de la Ruleta 
import random
import time


def tabla_numeros():
    tablero_ruleta=list(range(0,37))
    return tablero_ruleta

def eleccion_bola(tablero_ruleta):
    print("------------",tablero_ruleta,"-----------")
    bola=random.choice(tablero_ruleta)
    print("Esta es la bola que a salido:",bola)
    
        
    return bola


def numeros_jugador(tabla_numeros,saldo_ruleta):
    numeros=[]
    color=""
    estado=""
    combinada=[]
    print("1-Jugar a Colores")
    print("2-Jugar a Numeros")
    print("3-Jugar a Par/Impar")
    print("4-Hacer Combinadas")
    eleccion_player=int(input("Que modalidad quieres jugar?")) 
    
    while True:
        saldo_jugada=int(input("Cuanto dinero quieres meterle a tu jugada?"))
        if saldo_jugada>saldo_ruleta:
            print("La cantidad apostada es mayor que el saldo en tu cuenta,intentelo de nuevo...")
            continue
        else: 

            if eleccion_player==1:
                color_elegido=input("Rojo/Negro/Verde?")
                color=color_elegido
                
                
            elif eleccion_player ==2:
                jugadas=int(input("Cuantos numeros quieres seleccionar?"))
                while jugadas>0:
                    jugadas-=1
                    numeros_jugador=int(input("Que numeros quieres escojer?"))
                    numeros.append(numeros_jugador)
                    
            elif eleccion_player == 3:
                
                eleccion_pares=input("Elijes Par o Impar?")
                estado=eleccion_pares
                
            elif eleccion_player ==4:
                contador=int(input("Cuantas jugadas combindas deseas hacer?"))
                while contador>0:
                    
                    eleccion_combinada=input("Libre eleccion : NUM-0/36 , pares/impares , rojo/negro/verde")
                    combinada.append(eleccion_combinada)
                    longitud_dinero=len(combinada)
                    contador-=1
                    
            return numeros,color,estado,eleccion_player,saldo_jugada,combinada

def main_ruleta(saldo_total):
    print("""
    ******************************
    *                            *
    *       🎡  R U L E T A 🎡       *
    *                            *
    ******************************
    """)

    jugar=True
    saldo_ruleta=saldo_total
    while jugar and saldo_ruleta>0:
        
        tablero_ruleta=tabla_numeros()
        print("Tu Saldo:",saldo_ruleta,"$")
        numeros, color, estado,eleccion_player,saldo_jugada,combinada = numeros_jugador(tabla_numeros,saldo_ruleta)
        print("La bola se esta moviendo..")
        time.sleep(2)
        bola=eleccion_bola(tablero_ruleta)
        victoria=False
        
        if eleccion_player ==1:
            if bola%2==0 and bola>0:
                color_maquina="negro"
                if color_maquina==color:
                    print("Has acertado el Color")
                    victoria=True 
                else:
                    print("Has fallado,lo siento")
                    
                    
            else:
                color_maquina="rojo"
                if color_maquina==color:
                    print("Has acertado el color!!")
                    victoria=True
                else:
                    print("Has fallado,lo siento")
                    
                
        if eleccion_player==2:
            if bola in numeros:
                print("Has acertado!!")
                victoria=True
            else:
                print("Lo siento ,has fallado..")
                
        if eleccion_player==3:
            
            if bola%2==0 and bola>0:
                estado_maquina="par"
                if estado_maquina==estado:
                    print("Has acertado ,el numero era Par!!")
                    victoria=True
                else:
                    print("Has fallado,lo siento")
                    
                    
            else:
                estado_maquina="impar"
                if estado_maquina==estado:
                    print("Has acertado,el numero era impar!!")
                    victoria=True
                else:
                    print("Has fallado")
                    
        if eleccion_player==4:
            if bola%2==0 and bola>0:
                color_maquina="negro"
                if color_maquina==color:
                    print("Has acertado el Color")
                    victoria=True 
                else:
                    print("Has fallado,lo siento")
                    
                    
            else:
                color_maquina="rojo"
                if color_maquina==color:
                    print("Has acertado el color!!")
                    victoria=True
                else:
                    print("Has fallado,lo siento")
            if bola in numeros:
                print("Has acertado!!")
                victoria=True
            else:
                print("Lo siento ,has fallado..")
            if bola%2==0 and bola>0:
                estado_maquina="par"
                if estado_maquina==estado:
                    print("Has acertado ,el numero era Par!!")
                    victoria=True
                else:
                    print("Has fallado,lo siento")
                    
                    
            else:
                estado_maquina="impar"
                if estado_maquina==estado:
                    print("Has acertado,el numero era impar!!")
                    victoria=True
                else:
                    print("Has fallado")
            
        
        if victoria:
            saldo_ruleta+=saldo_jugada*2
            print("Tu Saldo:",saldo_ruleta,"$")
            seguir=input("Quieres continuar jugando?(s/n)")
            if seguir =="s":
                jugar=True
            else:
                jugar=False
        else:
            saldo_ruleta-=saldo_jugada
            print("Tu Saldo:",saldo_ruleta,"$")
            seguir=input("Quieres continuar jugando?(s/n)")
            if seguir =="s":
                jugar=True
            else:
                jugar=False

        if saldo_ruleta==0:
            print("Ya no tienes dinero,tendras que volver mas tarde,saliendo..")
            time.sleep(2)
            break
    print("Gracias por jugar a la ruleta ,volviendo al menu principal...")
    time.sleep(2)
    
    
## ME daba error y busque informacion sobre esto , no entiendo esto muy bien
if __name__ == "__main__":
    main_ruleta()

        


