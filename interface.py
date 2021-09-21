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

def critico1(monstuo:mobs):
    valor=random.randint(0,3)
    monstuo.vidaActual-=valor
    print("CRITICO ---> +"+str(valor))

def critico2(monstuo:mobs):
    valor=random.randint(1,4)
    monstuo.vidaActual-=valor
    print("CRITICO ---> +"+str(valor))

def critico3(monstuo:mobs):
    valor=random.randint(2,5)
    monstuo.vidaActual-=valor
    print("CRITICO ---> +"+str(valor))

def recuperarVida()-> None:
        usuario.vidaActual+=3
        if usuario.vidaActual > usuario.vidaMaxima:
            usuario.vidaActual=usuario.vidaMaxima

def seleccion():
    if aleatorio==0:
        print("Enemigo:"+Goblin.nombre)
        os.system("echo.")
        print("NIVEL:"+str(Goblin.nivel))
        os.system("echo.")
        print("Arma actual: "+Goblin.ARMA.nombreArma)
        os.system("echo.")
        print("Vida del enemigo:"+str(Goblin.vidaActual))
        os.system("echo.")
    elif aleatorio==1:
        print("Enemigo:"+Esqueleto.nombre)
        os.system("echo.")
        print("NIVEL:"+str(Esqueleto.nivel))
        os.system("echo.")
        print("Arma actual: "+Esqueleto.ARMA.nombreArma)
        os.system("echo.")
        print("Vida del enemigo:"+str(Esqueleto.vidaActual))
        os.system("echo.")

def estadoJugador():
    print("                                                                            EXP:"+str(usuario.experiencia)+"/"+str((10**(usuario.nivel+1))/2))
    print("                                                                            NIVEL:"+str(usuario.nivel))
    print("                                                                            Monedas:"+str(usuario.monedas))
    print("                                                                            Nombre de Usuario: "+nombreUsuario)
    print("                                                                            Arma actual: "+usuario.ARMA.nombreArma)
    print("                                                                            Vida actual: "+str(usuario.vidaActual))


def combate():
    while True:
            estadoJugador()
            seleccion()

            print("para atacar preisone\"A\"")
            os.system("echo.")
            print("para defenderse preisone\"B\"")
            os.system("echo.")
            print("para volver presione \"V\"")
            accion=input("ingrese una opcion:")

            if accion=="a" and aleatorio==0:
                os.system("cls")
                if usuario.critico==1:
                    critico1(Goblin)
                elif usuario.critico==2:
                    critico2(Goblin)
                elif usuario.critico==3:
                    critico3(Goblin)
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
                    print("MATASTE GOBLIN!")
                    print("+10 monedas")
                    usuario.monedas+=10
                    print("+40 EXP")
                    usuario.experiencia+=40
                    break
                recuperarVida()
            elif accion=="a" and aleatorio==1:
                os.system("cls")
                if usuario.critico==1:
                    critico1(Esqueleto)
                elif usuario.critico==2:
                    critico2(Esqueleto)
                elif usuario.critico==3:
                    critico3(Esqueleto)
                usuario.atacar(Esqueleto)
                print(usuario.ARMA.inflingedano)
                Esqueleto.atacar(usuario)
                print(Esqueleto.ARMA.inflingedano)
                if usuario.vidaActual==0:
                    os.system("cls")
                    print("¡¡PERDISTE!!")
                    break
                elif Esqueleto.vidaActual==0:
                    os.system("cls")
                    print("MATASTE ESQUELETO!")
                    print("+20 monedas")
                    usuario.monedas+=20
                    print("+75 EXP")
                    usuario.experiencia+=75
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==0:
                os.system("cls")
                Goblin.atacar(usuario)
                print(Goblin.ARMA.inflingedano)
                if usuario.vidaActual > 0:
                    usuario.vidaActual+=2
                if usuario.vidaActual==0:
                    os.system("cls")
                    print("¡¡PERDISTE!!")
                    break
                if Goblin.vidaActual==0:
                    print("¡MATASTE GOBLIN!")
                    print("+10 monedas")
                    usuario.monedas+=10
                    print("+40 EXP")
                    usuario.experiencia+=40
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==1:
                os.system("cls")
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
                    print("¡MATASTE ESQUELETO!")
                    print("+20 monedas")
                    usuario.monedas+=20
                    print("+75 EXP")
                    usuario.experiencia+=75
                    break
                recuperarVida()
            elif accion=="v":
                os.system("cls")
                break
            else:
                print("opcion incorrect vuelva a ingresar una opcion valida!")
                os.system("cls")
                continue

def tienda():
    while True:
        print("Para ir a la seccion de armas escriba\"armas\"")
        print("Para ir a la seccion de potenciadors escriba\"pot\"")
        print("para volver presione \"SALIR\"")
        eleccion=input("elija una opcion:")

        if eleccion=="armas":
            os.system("cls")
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
                else:
                    os.system("cls")
                    print("¡¡VOPCION INVALIDA!!")
                    os.system("echo.")
        elif eleccion=="pot":
            while True:
                os.system("cls")
                print("seleccione el ID del objeto a comprar!")
                print("para salir escriba\"salir\"")
                print("critico1 0-3 (crit_1) ---> 50 monedas")
                print("critico1 1-4 (crit_2) ---> 100 monedas")
                print("critico1 2-5 (crit_3) ---> 200 monedas")
                os.system("echo.")
                elec=input("ID:")
                if elec== "crit_1":
                    os.system("cls")
                    usuario.monedas-=50
                    usuario.critico=1
                    continue
                elif elec=="crit_2":
                    os.system("cls")
                    usuario.monedas-=100
                    usuario.critico=2
                    continue
                elif elec=="crit_3":
                    os.system("cls")
                    usuario.monedas-=200
                    usuario.critico=3
                    continue
                elif elec=="salir":
                    os.system("cls")
                    break
        elif eleccion=="salir":
            os.system("cls")
            break
        else:
            os.system("cls")
            print("OPCION INVALIDA!")
            continue


def Mochila():
    while True:
        print("Para desequipar presione \"D\"")
        print("Para equipar presione \"E\"")
        print("para volver presione \"V\"")

        print(mochila)

        opcion=input("Elija una opcion:")

        if opcion=="d":
            print("nombre del objeto a desequipar:")
            print("arma equipada: ["+usuario.ARMA.nombreArma+"]")
            os.system("echo.")
            opcion1=input("nombre:")
            if opcion1== "espada":
                if usuario.ARMA==vacio or usuario.ARMA != espada:
                    os.system("cls")
                    print("opcion invalida!!")
                    continue
                usuario.ARMA=vacio
                mochila.append(espada.nombreArma)
            elif opcion1=="arco":
                if usuario.ARMA==vacio or usuario.ARMA != arco:
                    os.system("cls")
                    print("opcion invalida!!")
                    continue
                usuario.ARMA=vacio
                mochila.append(arco.nombreArma)
            elif opcion1=="hacha":
                if usuario.ARMA==vacio or usuario.ARMA != hacha:
                    os.system("cls")
                    print("opcion invalida!!")
                    continue
                usuario.ARMA=vacio
                mochila.append(hacha.nombreArma)
            elif opcion1=="katana":
                if usuario.ARMA==vacio or usuario.ARMA != katana:
                    os.system("cls")
                    print("opcion invalida!!")
                    continue
                usuario.ARMA=vacio
                mochila.append(katana.nombreArma)
            elif opcion1=="martillo":
                if usuario.ARMA==vacio or usuario.ARMA != martillo:
                    os.system("cls")
                    print("opcion invalida!!")
                    continue
                usuario.ARMA=vacio
                mochila.append(martillo.nombreArma)
            elif opcion1=="esapda-inteligente":
                if usuario.ARMA==vacio or usuario.ARMA != samrtSword:
                    os.system("cls")
                    print("opcion invalida!!")
                    continue
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
                if espada not in mochila:
                    os.system("cls")
                    print("OPCION INVALIDA")
                    continue
                usuario.ARMA=espada
                mochila.remove(espada.nombreArma)
                os.system("cls")
            elif opcion2=="arco":
                if arco not in mochila:
                    os.system("cls")
                    print("OPCION INVALIDA")
                    continue
                usuario.ARMA=arco
                mochila.remove(arco.nombreArma)
                os.system("cls")
            elif opcion2=="hacha":
                if hacha not in mochila:
                    os.system("cls")
                    print("OPCION INVALIDA")
                    continue
                usuario.ARMA=hacha
                mochila.remove(hacha.nombreArma)
                os.system("cls")
            elif opcion2=="katana":
                if katana not in mochila:
                    os.system("cls")
                    print("OPCION INVALIDA")
                    continue
                usuario.ARMA=katana
                mochila.remove(katana.nombreArma)
                os.system("cls")
            elif opcion2=="martillo":
                if martillo not in mochila:
                    os.system("cls")
                    print("OPCION INVALIDA")
                    continue
                usuario.ARMA=martillo
                mochila.remove(martillo.nombreArma)
                os.system("cls")
            elif opcion2=="esapda_inteligente":
                if samrtSword not in mochila:
                    os.system("cls")
                    print("OPCION INVALIDA")
                    continue
                usuario.ARMA=samrtSword
                mochila.remove(samrtSword.nombreArma)
                os.system("cls")
        elif opcion=="v":
            os.system("cls")
            break

def nivel():
    if usuario.experiencia>=(10**2)/2 and usuario.experiencia<(10**3)/2:
        usuario.experiencia=0
        usuario.nivel=2
        usuario.vidaMaxima=22
        usuario.vidaActual=usuario.vidaMaxima
        print(" ¡¡FELICIDADES HAS SUBIDO AL NIVEL \"2\"!!")
    elif usuario.experiencia>=(10**3)/2 and usuario.experiencia<(10**4)/2:
        usuario.experiencia=0
        usuario.nivel=3
        usuario.vidaMaxima=25
        usuario.vidaActual=usuario.vidaMaxima
        print(" ¡¡FELICIDADES HAS SUBIDO AL NIVEL \"3\"!!")
    elif usuario.experiencia>=(10**4)/2 and usuario.experiencia<(10**5)/2:
        usuario.experiencia=0
        usuario.nivel=4
        usuario.vidaMaxima=27
        usuario.vidaActual=usuario.vidaMaxima
        print(" ¡¡FELICIDADES HAS SUBIDO AL NIVEL \"4\"!!")
    elif usuario.experiencia>=(10**5)/2:
        usuario.experiencia=0
        usuario.nivel=5
        usuario.vidaMaxima=30
        usuario.vidaActual=usuario.vidaMaxima
        print(" ¡¡FELICIDADES HAS SUBIDO AL NIVEL \"5\"!!")

while True:

    while True:
        nivel()
        Goblin.vidaActual=Goblin.vidaMaxima
        Esqueleto.vidaActual=Esqueleto.vidaMaxima
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
        elif parametro=="t":
            os.system("cls")
            tienda()
        elif parametro=="m":
            os.system("cls")
            Mochila()
        else:
            os.system("cls")
            print("OPCION INVALIDA!!")
            break
  
