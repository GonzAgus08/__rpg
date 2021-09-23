from math import comb
from monstruo import *
import os
import random 

aleatorio=random.randint(0,3)

mochila=[]
mochila1=[]

Goblin=goblin(None,None,None,vacia,vacia,vacia,vacia,vacia)
Goblin5=goblin5(None,None,None,vacia,vacia,vacia,vacia,escudoHierro)
Esqueleto=squeleton(None,None,None,vacia,vacia,vacia,vacia,vacia)
Esqueleto5=squeleton5(None,None,None,cascoCuero,vacia,vacia,vacia,escudoHierro)

nombreUsuario=input("ingrese su nombre de Usuario:")
os.system("cls")

usuario=Jugador(20,hacha,nombreUsuario,vacia,vacia,vacia,vacia,vacia)


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

def mostraRegeneracion() -> int:
    pibote=usuario.vidaActual
    pibote2=usuario.vidaActual=1
    recuperarVida()
    valor=usuario.vidaActual-pibote2
    usuario.vidaActual=pibote
    return valor

def comanSeleccion(monstruo: 'mobs'):
    print("Enemigo:"+monstruo.nombre)
    os.system("echo.")
    print("NIVEL:"+str(monstruo.nivel))
    os.system("echo.")
    print("Arma actual: "+monstruo.ARMA.nombreArma)
    os.system("echo.")
    print("Vida del enemigo:"+str(monstruo.vidaActual))
    os.system("echo.")

def seleccion():
    if aleatorio==0:
        comanSeleccion(Goblin)
    elif aleatorio==1:
        comanSeleccion(Esqueleto)
    elif aleatorio==2:
        comanSeleccion(Goblin5)
    elif aleatorio==3:
        comanSeleccion(Esqueleto5)

def estadoJugador():
    print(f"                                                                            Nombre de Usuario: {nombreUsuario}")
    print(f"                                                                            Vida actual: {usuario.vidaActual}")
    print("                                                                            EXP: "+str(usuario.experiencia)+"/"+str((10**(usuario.nivel+1)/2)))
    print(f"                                                                            NIVEL: {usuario.nivel}")
    print(f"                                                                            Monedas: {usuario.monedas}")
    print(f"                                                                            Arma actual: {usuario.ARMA.nombreArma}")
    print(f"                                                                            casco: {usuario.casco.nombreArmadura}")
    print(f"                                                                            pecho:{usuario.pecho.nombreArmadura}")
    print(f"                                                                            piernas:{usuario.piernas.nombreArmadura}")
    print(f"                                                                            pies:{usuario.pies.nombreArmadura}")
    print(f"                                                                            escudo:{usuario.escudo.nombreArmadura}")

def comanCobat(monstruo: 'mobs'):
    os.system("cls")
    pibote=usuario.vidaActual
    if usuario.critico==1:
        critico1(monstruo)
    elif usuario.critico==2:
        critico2(monstruo)
    elif usuario.critico==3:
        critico3(monstruo)
    usuario.atacar(monstruo)
    print(usuario.ARMA.inflingedano)
    os.system("echo.")
    monstruo.atacar(usuario)
    print(monstruo.ARMA.inflingedano)
    os.system("echo.")
    pibote2=-(usuario.vidaActual-pibote)
    print(f"daño recibido: {pibote2}")
    os.system("echo.")
    regeneracion=mostraRegeneracion()
    print(f"regeneracion: {regeneracion}")

def comanComand2(monstruo: 'mobs'):
    os.system("cls")
    pibote=usuario.vidaActual
    monstruo.atacar(usuario)
    print(monstruo.ARMA.inflingedano)
    os.system("echo.")
    pibote2=-(usuario.vidaActual-pibote)
    print(f"daño recibido: {pibote2}")
    os.system("echo.")
    if usuario.vidaActual>0:
        regeneracion=mostraRegeneracion()
        print(f"regeneracion: {regeneracion}")

def dialogoDefeat():
    print("¡¡PERDISTE!!")
    input("PRESIONE CUALQUIER TECLA...")
    os.system("cls")

def dialogoWin(palabrin,monedas,exp):
    print(f"MATASTE {palabrin}!")
    print(f"+{monedas} monedas")
    usuario.monedas+=monedas
    print(f"+{exp} EXP")
    usuario.experiencia+=exp
    input("PRESIONE CUALQUIER TECLA...")
    os.system("cls")

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
                comanCobat(Goblin)
                if usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                elif Goblin.vidaActual==0:
                    dialogoWin("GOBLIN",10,40)
                    break
                recuperarVida()
            elif accion=="a" and aleatorio==1:
                comanCobat(Esqueleto)
                if usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                elif Esqueleto.vidaActual==0:
                    dialogoWin("ESQUELETO",20,75)
                    break
                recuperarVida()
            elif accion=="a" and aleatorio==2:
                comanCobat(Goblin5)
                if usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                elif Goblin.vidaActual==0:
                    dialogoWin("GOBLIN",35,100)
                    break
                recuperarVida()
            elif accion=="a" and aleatorio==3:
                comanCobat(Esqueleto5)
                if usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                elif Goblin.vidaActual==0:
                    dialogoWin("ESQUELETO",50,150)
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==0:
                comanComand2(Goblin)
                if usuario.vidaActual > 0:
                    usuario.vidaActual+=2
                elif usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                if Goblin.vidaActual==0:
                    dialogoWin("GOBLIN",10,40)
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==1:
                comanComand2(Esqueleto)
                if usuario.vidaActual > 0:
                    usuario.vidaActual+=2
                elif usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                if Esqueleto.vidaActual==0:
                    dialogoWin("ESQUELETO",20,75)
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==2:
                comanComand2(Goblin5)
                if usuario.vidaActual > 0:
                    usuario.vidaActual+=2
                elif usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                if Goblin.vidaActual==0:
                    dialogoWin("GOBLIN",35,100)
                    break
                recuperarVida()
            elif accion=="b" and aleatorio==3:
                comanComand2(Esqueleto5)
                if usuario.vidaActual > 0:
                    usuario.vidaActual+=2
                elif usuario.vidaActual==0:
                    dialogoDefeat()
                    break
                if Goblin.vidaActual==0:
                    dialogoWin("ESQUELETO",50,150)
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
        os.system("echo.")
        print("Para ir a la seccion de armaduras escriba\"armaduras\"")
        os.system("echo.")
        print("Para ir a la seccion de potenciadors escriba\"pot\"")
        os.system("echo.")
        print("para volver presione \"SALIR\"")
        eleccion=input("elija una opcion:")

        if eleccion=="armaduras":
            os.system("cls")
            while True:
                print("*************************ARMADURAS*************************")
                estadoJugador()

                print("Seleccione el ID del objeto que quiere comprar:")
                print("para volver presione \"SALIR\"")
                os.system("echo.")

                print("ID: c_cu (casco de cuero) ---> precio 30 monedas.")
                print("ID: ch_cu (chaleco de cuero) ---> precio 50 monedas.")
                print("ID: p_cu (piernas de cuero) ---> precio 40 monedas.")
                print("ID: b_cu (botas de cuero) ---> precio 30 monedas.")
                print("ID: s_ir (escudo de hiero) ---> precio 50 monedas.")
                os.system("echo.")

                print(mochila1)
                os.system("echo.")

                accion=input("elija una opcion:")

                if accion=="c_cu":
                    if usuario.monedas < 30:
                        os.system("cls")
                        print("monedas insuficientes!!")
                        continue
                    mochila1.append(cascoCuero.nombreArmadura)
                    usuario.monedas-=30
                    os.system("cls")
                elif accion=="salir":
                    os.system("cls")
                    break
                elif accion=="ch_cu":
                    if usuario.monedas < 50:
                        os.system("cls")
                        print("monedas insuficientes!!")
                        continue
                    mochila1.append(chalecoCuero.nombreArmadura)
                    usuario.monedas-=50
                    os.system("cls")
                elif accion=="p_cu":
                    if usuario.monedas < 40:
                        os.system("cls")
                        print("monedas insuficientes!!")
                        continue
                    mochila1.append(piernasCuero.nombreArmadura)
                    usuario.monedas-=40
                    os.system("cls")
                elif accion=="b_cu":
                    if usuario.monedas <30:
                        os.system("cls")
                        print("monedas insuficientes!!")
                        continue
                    mochila1.append(botasCuero.nombreArmadura)
                    usuario.monedas-=30
                    os.system("cls")
                elif accion=="s_ir":
                    if usuario.monedas < 50:
                        os.system("cls")
                        print("monedas insuficientes!!")
                        continue
                    mochila1.append(escudoHierro.nombreArmadura)
                    usuario.monedas-=50
                    os.system("cls")
                else:
                    os.system("cls")
                    print("¡¡OPCION INVALIDA!!")
                    os.system("echo.")

        elif eleccion=="armas":
            os.system("cls")
            while True:
                print("*************************ARMAS*************************")
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
                    print("¡¡OPCION INVALIDA!!")
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

        print(f"ARMAS: {mochila}")
        print(f"ARMADURAS: {mochila1}")

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
            os.system("cls")
            print("para equipar armadura escriba\"ARMADURA\"")
            print("para equipar arma escriba\"ARMA\"")

            definir=input("seleccion su opcion:")
            
            if definir=="arma":
                if usuario.ARMA != vacio:
                    mochila.append(usuario.ARMA.nombreArma)
                    usuario.ARMA=vacio
                print(f"ARMAS:{mochila}")
                os.system("echo.")
                opcion2=input("nombre del objeto a equipar:")
                if opcion2== "espada":
                    if espada.nombreArma not in mochila:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.ARMA=espada
                    mochila.remove(espada.nombreArma)
                    os.system("cls")
                elif opcion2=="arco":
                    if arco.nombreArma not in mochila:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.ARMA=arco
                    mochila.remove(arco.nombreArma)
                    os.system("cls")
                elif opcion2=="hacha":
                    if hacha.nombreArma not in mochila:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.ARMA=hacha
                    mochila.remove(hacha.nombreArma)
                    os.system("cls")
                elif opcion2=="katana":
                    if katana.nombreArma not in mochila:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.ARMA=katana
                    mochila.remove(katana.nombreArma)
                    os.system("cls")
                elif opcion2=="martillo":
                    if martillo.nombreArma not in mochila:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.ARMA=martillo
                    mochila.remove(martillo.nombreArma)
                    os.system("cls")
                elif opcion2=="esapda_inteligente":
                    if samrtSword.nombreArma not in mochila:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.ARMA=samrtSword
                    mochila.remove(samrtSword.nombreArma)
                    os.system("cls")
                else:
                    os.system("cls")
                    print("OPCION INVALIDA!")
                    continue
            elif definir=="armadura":
                print(f"ARMADURAS:{mochila1}")
                os.system("echo.")
                opcion2=input("nombre del objeto a equipar:")
                if opcion2== "casco de cuero":
                    if usuario.casco != vacia:
                        mochila1.append(usuario.casco.nombreArmadura)
                        usuario.ARMA=vacia
                    if cascoCuero.nombreArmadura not in mochila1:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.casco=cascoCuero
                    mochila1.remove(cascoCuero.nombreArmadura)
                    os.system("cls")
                elif opcion2=="chaleco de cuero":
                    if usuario.pecho != vacia:
                        mochila1.append(usuario.pecho.nombreArmadura)
                        usuario.pecho=vacia
                    if chalecoCuero.nombreArmadura not in mochila1:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.pecho=chalecoCuero
                    mochila1.remove(chalecoCuero.nombreArmadura)
                    os.system("cls")
                elif opcion2=="piernas de cuero":
                    if usuario.piernas != vacia:
                        mochila1.append(usuario.piernas.nombreArmadura)
                        usuario.piernas=vacia
                    if piernasCuero.nombreArmadura not in mochila1:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.piernas=piernasCuero
                    mochila1.remove(piernasCuero.nombreArmadura)
                    os.system("cls")
                elif opcion2=="botas de cuero":
                    if usuario.pies != vacia:
                        mochila1.append(usuario.pies.nombreArmadura)
                    usuario.ARMA=vacia
                    if botasCuero.nombreArmadura not in mochila1:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.pies=botasCuero
                    mochila1.remove(botasCuero.nombreArmadura)
                    os.system("cls")
                elif opcion2=="escudo de hierro":
                    if escudoHierro.nombreArmadura not in mochila1:
                        os.system("cls")
                        print("OPCION INVALIDA")
                        continue
                    usuario.escudo=escudoHierro
                    mochila1.remove(escudoHierro.nombreArmadura)
                    os.system("cls")
            else:
                os.system("cls")
                print("OPCION INVALIDA!")
                continue
        elif opcion=="v":
            os.system("cls")
            break
        else:
            os.system("cls")
            print("OPCION INVALIDA!")
            continue

def comanLevel(nivelote,vidamaxima,ataquebase,aumentovida):
    if usuario.experiencia>=(10**nivelote)/2 and usuario.experiencia<(10**(nivelote+1))/2:
        usuario.experiencia=0
        usuario.nivel=nivelote
        usuario.vidaMaxima=vidamaxima
        usuario.vidaActual=usuario.vidaMaxima
        usuario.ataqueBase=ataquebase
        print(" ¡¡FELICIDADES HAS SUBIDO AL NIVEL \"2\"!!")
        os.system("echo.")
        print("*****BONUS DE NIVEL*****")
        print(f"-vida maxima: +{aumentovida}")
        print(f"-ataque base: +{ataquebase}")

def nivel():
    if usuario.nivel==1:
        comanLevel(2,22,1,2)
    elif usuario.nivel==2:
        comanLevel(3,25,2,3)
    elif usuario.nivel==3:
        comanLevel(4,27,3,2)
    elif usuario.nivel==4:
        comanLevel(5,30,4,3)

def main() -> None:
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
    
if __name__=='__main__':
    main()
