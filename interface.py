from math import comb
from monstruo import *
import os
import random 

aleatorio=random.randint(0,1)

mochila=[]

Goblin=goblin(None,None,None)
Esqueleto=squeleton(None,None,None)

nombreUsuario=input("ingrese su nombre de Usuario:")
os.system("cls")

usuario=Jugador(20,hacha,nombreUsuario)

def critico(monstuo:mobs):
    if critico=="si":
        monstuo.vidaActual=monstuo.vidaActual-random.randint(0,3)

def recuperarVida()-> None:
        usuario.vidaActual+=3
        if usuario.vidaActual > usuario.vidaMaxima:
            usuario.vidaActual=usuario.vidaMaxima

def seleccion():
    if aleatorio==0:
        print("Enemigo:"+Goblin.nombre)
        os.system("echo.")
        print("Arma actual: "+Goblin.ARMA.nombreArma)
        os.system("echo.")
        print("Vida del enemigo:"+str(Goblin.vidaActual))
        os.system("echo.")
    elif aleatorio==1:
        print("Enemigo:"+Esqueleto.nombre)
        os.system("echo.")
        print("Arma actual: "+Esqueleto.ARMA.nombreArma)
        os.system("echo.")
        print("Vida del enemigo:"+str(Esqueleto.vidaActual))
        os.system("echo.")

def estadoJugador():
    print("                                                                            Monedas:"+str(usuario.monedas))
    print("                                                                            Nombre de Usuario: "+nombreUsuario)
    print("                                                                            Arma actual: "+usuario.ARMA.nombreArma)
    print("                                                                            Vida actual: "+str(usuario.vidaActual))


def combate():
    while True:
            estadoJugador()
            seleccion()

            Goblin.vidaActual=Goblin.vidaMaxima
            Esqueleto.vidaActual=Esqueleto.vidaMaxima

            print("para atacar preisone\"A\"")
            os.system("echo.")
            print("para defenderse preisone\"B\"")
            os.system("echo.")
            print("para volver presione \"V\"")
            accion=input("ingrese una opcion:")

            if accion=="a" and aleatorio==0:
                usuario.atacar(Goblin)
                print(usuario.ARMA.inflingedano)
                Goblin.atacar(usuario)
                print(Goblin.ARMA.inflingedano)
                if usuario.vidaActual==0:
                    os.system("cls")
                    print("¡¡PERDISTE!!")
                    break
                elif Goblin.vidaActual==0:
                    os.system("cls")
                    print("mataste a Goblin")
                    print("+10 monedas")
                    usuario.monedas+=10
                    break
                recuperarVida()
            elif accion=="a" and aleatorio==1:
                usuario.atacar(Goblin)
                print(usuario.ARMA.inflingedano)
                Esqueleto.atacar(usuario)
                print(Esqueleto.ARMA.inflingedano)
                if usuario.vidaActual==0:
                    os.system("cls")
                    print("¡¡PERDISTE!!")
                    break
                elif Esqueleto.vidaActual==0:
                    os.system("cls")
                    print("mataste a Esqueleto")
                    print("+20 monedas")
                    usuario.monedas+=20
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==0:
                Goblin.atacar(usuario)
                print(Goblin.ARMA.inflingedano)
                if usuario.vidaActual > 0:
                    usuario.vidaActual+=2
                if usuario.vidaActual==0:
                    os.system("cls")
                    print("¡¡PERDISTE!!")
                    break
                if Goblin.vidaActual==0:
                    print("mataste a Goblin")
                    print("+10 monedas")
                    usuario.monedas+=10
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==1:
                Esqueleto.atacar(usuario)
                print(Esqueleto.ARMA.inflingedano)
                if usuario.vidaActual > 0:
                    usuario.vidaActual+=2
                if usuario.vidaActual==0:
                    os.system("cls")
                    print("¡¡PERDISTE!!")
                    break
                if Esqueleto.vidaActual==0:
                    os.system("cls")
                    print("mataste a Esqueleto")
                    print("+20 monedas")
                    usuario.monedas+=20
                    break
                recuperarVida()
            elif accion=="v":
                os.system("cls")
                break
            else:
                print("opcion incorrect vuelva a ingresar una opcion valida!")
                os.system("cls")
                continue
            os.system("cls")

def tienda():
    while True:
        estadoJugador()

        print("Seleccione el ID del objeto que quiere comprar:")
        print("para volver presione \"SALIR\"")
        os.system("echo.")

        print("ID: esp (espada) ---> precio 30 monedas.")
        print("ID: arc (arco) ---> precio 50 monedas.")
        print("ID: ach (hacha) ---> precio 75 monedas.")
        print("ID: ktn (katana) ---> precio 150 monedas.")
        print("ID: mrt (martillo) ---> precio 250 monedas.")
        print("ID: smw (espada intelgente) ---> precio 600 monedas.")
        os.system("echo.")

        print(mochila)
        os.system("echo.")

        accion=input("elija una opcion:")

        if accion=="esp":
            if usuario.monedas < 30:
                os.system("cls")
                print("monedas insuficientes!!")
                continue
            mochila.append(espada.nombreArma)
            usuario.monedas-=30
            os.system("cls")
        elif accion=="salir":
            os.system("cls")
            while True:
                estadoJugador()
                os.system("echo.")
                print("para combatir presione \"w\"")
                print("para ir a la tienda presione \"T\"")
                print("para ir a la mochila presione \"M\"")
                parametro=input("ingrese una accion:")
                if parametro=="w":
                    os.system("cls")
                    combate()
                if parametro=="t":
                    os.system("cls")
                    tienda()
                if parametro=="m":
                    os.system("cls")
                    Mochila()
                else:
                    break
    
        elif accion=="arc":
            if usuario.monedas < 50:
                os.system("cls")
                print("monedas insuficientes!!")
                continue
            mochila.append(arco.nombreArma)
            usuario.monedas-=50
            os.system("cls")
        elif accion=="ach":
            if usuario.monedas < 75:
                os.system("cls")
                print("monedas insuficientes!!")
                continue
            mochila.append(hacha.nombreArma)
            usuario.monedas-=75
            os.system("cls")
        elif accion=="ktn":
            if usuario.monedas < 150:
                os.system("cls")
                print("monedas insuficientes!!")
                continue
            mochila.append(katana.nombreArma)
            usuario.monedas-=150
            os.system("cls")
        elif accion=="mrt":
            if usuario.monedas < 250:
                os.system("cls")
                print("monedas insuficientes!!")
                continue
            mochila.append(martillo.nombreArma)
            usuario.monedas-=250
            os.system("cls")
        elif accion=="smw":
            if usuario.monedas < 600:
                os.system("cls")
                print("monedas insuficientes!!")
                continue
            mochila.append(samrtSword.nombreArma)
            usuario.monedas-=600
            os.system("cls")

def Mochila():
    while True:
        print("Para desequipar presione \"D\"")
        print("Para equipar presione \"E\"")
        print("para volver presione \"V\"")

        print(mochila)

        opcion=input("Elija una opcion:")

        if opcion=="d":
            print("nombre del objeto a desequipar:")
            os.system("echo.")
            opcion1=input("nombre:")
            if opcion1== "espada":
                usuario.ARMA=vacio
                mochila.append(espada.nombreArma)
            elif opcion1=="arco":
                usuario.ARMA=vacio
                mochila.append(arco.nombreArma)
            elif opcion1=="hacha":
                usuario.ARMA=vacio
                mochila.append(hacha.nombreArma)
            elif opcion1=="katana":
                usuario.ARMA=vacio
                mochila.append(katana.nombreArma)
            elif opcion1=="martillo":
                usuario.ARMA=vacio
                mochila.append(martillo.nombreArma)
            elif opcion1=="esapda inteligente":
                usuario.ARMA=vacio
                mochila.append(samrtSword.nombreArma)
            elif usuario.ARMA==vacio:
                os.system("cls")
                print("ya esta vacio el lote!!")
                continue
        elif opcion=="e":
            if usuario.ARMA != vacio:
                mochila.append(usuario.ARMA.nombreArma)
                usuario.ARMA=vacio
            print("nombre del objeto a equipar:")
            os.system("echo.")
            opcion2=input("nombre:")
            if opcion2== "espada":
                usuario.ARMA=espada
                mochila.remove(espada.nombreArma)
            elif opcion2=="arco":
                usuario.ARMA=arco
                mochila.remove(arco.nombreArma)
            elif opcion2=="hacha":
                usuario.ARMA=hacha
                mochila.remove(hacha.nombreArma)
            elif opcion2=="katana":
                usuario.ARMA=katana
                mochila.remove(katana.nombreArma)
            elif opcion2=="martillo":
                usuario.ARMA=martillo
                mochila.remove(martillo.nombreArma)
            elif opcion2=="esapda inteligente":
                usuario.ARMA=samrtSword
                mochila.remove(samrtSword.nombreArma)
        elif opcion=="v":
            os.system("cls")
            break
    


while True:
    usuario.vidaActual=usuario.vidaMaxima
    estadoJugador()
    os.system("echo.")
    print("para combatir presione \"w\"")
    print("para ir a la tienda presione \"T\"")
    print("para ir a la mochila presione \"M\"")
    parametro=input("ingrese una accion:")
    if parametro=="w":
        os.system("cls")
        combate()
    if parametro=="t":
        os.system("cls")
        tienda()
    if parametro=="m":
        os.system("cls")
        Mochila()
    else:
        break
    
