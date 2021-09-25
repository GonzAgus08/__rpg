from monstruo import *
import os
import random

mochilaClases=["mago","aquero","guerrero","berserker"]

def charlantina() -> None:
    os.system("cls")
    print("OPCION INVALIDA!!")
    print("por favor, ingrese una opcion valida.")
    os.system("echo.")

def stats(
    casco: 'armadura',
    pecho: 'armadura',
    piernas: 'armadura',
    pies: 'armadura',
    escudo: 'armadura',
    clase:str,
    vidaMaxima:int,
    ARMA: 'arma',
    ataqueBase:int,
    defensaBase:int
    ) -> None:
    mochilon=[
        casco.nombreArmadura,
        pecho.nombreArmadura,
        piernas.nombreArmadura,
        pies.nombreArmadura,
        escudo.nombreArmadura
    ]
    os.system("echo.")
    print(clase)
    print(vidaMaxima)
    print(ARMA)
    print(f"ARMADURAS: {mochilon}")
    print(f"ATAQUE BASE: {ataqueBase}")
    print(f"DEFENSA BASE: {defensaBase}")
    os.system("echo.")


nombreUsuario=input("ingrese su nombre de Usuario:")
os.system("cls")
print("CLASES:")
print(mochilaClases)
stats(cascoCuero,vacia,vacia,vacia,vacia,"MAGO",18,cetroMagico.nombreArma,4,0)
stats(vacia,vacia,vacia,vacia,vacia,"GUERRERO",22,espadaHierro.nombreArma,0,2)
stats(vacia,vacia,vacia,botasCuero,vacia,"ARQUERO",20,arcoPlatinado.nombreArma,1,1)
stats(vacia,vacia,vacia,vacia,vacia,"BERSERKER",22,hacha.nombreArma,2,0)
clase=input("elija la clase de su personaje:")
os.system("cls")

while True:
    if clase=="mago" or clase=="MAGO": 
        usuario=Jugador(18,cetroMagico,nombreUsuario,cascoCuero,vacia,vacia,vacia,vacia)
        usuario.ataqueBase=4
        break
    elif clase=="guerrero" or clase=="GUERRERO":
        usuario=Jugador(22,espadaHierro,nombreUsuario,vacia,vacia,vacia,vacia,vacia)
        usuario.defensaBase=2
        break
    elif clase=="arquero" or clase=="ARQUERO":
        usuario=Jugador(20,arcoPlatinado,nombreUsuario,vacia,vacia,vacia,botasCuero,vacia)
        usuario.defensaBase=1
        usuario.ataqueBase=1
        break
    elif clase=="berserker" or "BERSERKER":
        usuario=Jugador(22,hacha,nombreUsuario,vacia,vacia,vacia,vacia,vacia)
        usuario.ataqueBase=2
        break
    else:
        charlantina()
        continue
    

mochila=[]
mochila1=[]
enemigos=[
    ["Goblin --- NIVEL: 1 --- NIVEL: 5",
    "Esqueleto --- NIVEL: 1 --- NIVEL: 5"],
    ["Escorpion --- NIVEL: 1 --- NIVEL: 5",
    "Minotauro --- NIVEL: 1 --- NIVEL: 5"]
    ]

Goblin=goblin(None,None,None,vacia,vacia,vacia,vacia,vacia)
Goblin5=goblin5(None,None,None,vacia,vacia,vacia,vacia,escudoHierro)
Esqueleto=squeleton(None,None,None,vacia,vacia,vacia,vacia,vacia)
Esqueleto5=squeleton5(None,None,None,cascoCuero,vacia,vacia,vacia,escudoHierro)
Escorpion=scorpion(None,None,None,vacia,vacia,piernasCuero,botasCuero,vacia)
Escorpion5=scorpion5(None,None,None,cascoCuero,vacia,piernasCuero,botasCuero,vacia)
Minotauro=minotauro(None,None,None,cascoCuero,chalecoCuero,vacia,vacia,escudoHierro)
Minotauro5=minotauro5(None,None,None,cascoCuero,chalecoCuero,piernasCuero,vacia,escudoHierro)

def comanSeleccion(monstruo: 'mobs') -> None:
    print("Enemigo:"+monstruo.nombre)
    os.system("echo.")
    print("NIVEL:"+str(monstruo.nivel))
    os.system("echo.")
    print("Arma actual: "+monstruo.ARMA.nombreArma)
    os.system("echo.")
    print("Vida del enemigo:"+str(monstruo.vidaActual))
    os.system("echo.")

def seleccion(aleatorio:int,divicion:int) -> None:
    if divicion==1:
        if aleatorio==0:
            comanSeleccion(Goblin)
        elif aleatorio==1:
            comanSeleccion(Goblin5)
        elif aleatorio==2:
            comanSeleccion(Esqueleto)
        elif aleatorio==3:
            comanSeleccion(Esqueleto5)
    elif divicion==2:
        if aleatorio==0:
            comanSeleccion(Escorpion)
        elif aleatorio==1:
            comanSeleccion(Escorpion5)
        elif aleatorio==2:
            comanSeleccion(Minotauro)
        elif aleatorio==3:
            comanSeleccion(Minotauro5)

def comanCobat(monstruo: 'mobs') -> None:
    os.system("cls")
    pibote=usuario.vidaActual
    piboteM=monstruo.vidaActual
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
    pibote2m=-(monstruo.vidaActual-piboteM)
    print(f"daño inflingido: {pibote2m}")
    os.system("echo.")
    regeneracion=mostraRegeneracion()
    print(f"regeneracion: {regeneracion}")

def comanComand2(monstruo: 'mobs') -> None:
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

def dialogoDefeat() -> None:
    print("¡¡PERDISTE!!")
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
    os.system("cls")

def dialogoWin(palabrin:str,monedas:int,exp:int) -> None:
    print(f"MATASTE A {palabrin}!")
    print(f"+{monedas} monedas")
    usuario.monedas+=monedas
    print(f"+{exp} EXP")
    usuario.experiencia+=exp
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
    os.system("cls")


def mapas(
    monstruo1: 'mobs',
    monedas1: int,
    expe1:int, 
    monstruo2: 'mobs',
    monedas2: int,
    expe2: int, 
    monstruo3: 'mobs',
    monedas3:int,
    expe3:int, 
    monstruo4: 'mobs',
    monedas4:int,
    expe4:int,
    divicion:int) -> None:
    while True:

        aleatorio=random.randint(0,3)
        estadoJugador()
        seleccion(aleatorio,divicion)

        print("para atacar preisone\"A\"")
        os.system("echo.")
        print("para defenderse preisone\"B\"")
        os.system("echo.")
        print("para volver presione \"V\"")
        accion=input("ingrese una opcion:")

        if (accion=="a" or accion=="A") and aleatorio==0:
            comanCobat(monstruo1)
            if usuario.vidaActual==0:
                dialogoDefeat()
                break
            elif monstruo1.vidaActual==0:
                dialogoWin(monstruo1.nombre,monedas1,expe1)
                break
            recuperarVida()
        elif (accion=="a" or accion=="A") and aleatorio==1:
            comanCobat(monstruo2)
            if usuario.vidaActual==0:
                dialogoDefeat()
                break
            elif monstruo2.vidaActual==0:
                dialogoWin(monstruo2.nombre,monedas2,expe2)
                break
            recuperarVida()
        elif (accion=="a" or accion=="A") and aleatorio==2:
            comanCobat(monstruo3)
            if usuario.vidaActual==0:
                dialogoDefeat()
                break
            elif monstruo3.vidaActual==0:
                dialogoWin(monstruo3.nombre,monedas3,expe3)
                break
            recuperarVida()
        elif (accion=="a" or accion=="A") and aleatorio==3:
            comanCobat(monstruo4)
            if usuario.vidaActual==0:
                dialogoDefeat()
                break
            elif monstruo4.vidaActual==0:
                dialogoWin(monstruo4,monedas4,expe4)
                break
            recuperarVida()
        elif (accion=="b" or accion=="B") and aleatorio==0:
            comanComand2(monstruo1)
            if usuario.vidaActual > 0:
                usuario.vidaActual+=2
            elif usuario.vidaActual==0:
                dialogoDefeat()
                break
            if monstruo1.vidaActual==0:
                dialogoWin(monstruo1.nombre,monedas1,expe1)
                break
            recuperarVida()
        elif (accion=="b" or accion=="B") and aleatorio==1:
            comanComand2(monstruo2)
            if usuario.vidaActual > 0:
                usuario.vidaActual+=2
            elif usuario.vidaActual==0:
                dialogoDefeat()
                break
            if monstruo2.vidaActual==0:
                dialogoWin(monstruo2.nombre,monedas2,expe2)
                break
            recuperarVida()
        elif (accion=="B" or accion=="b") and aleatorio==2:
            comanComand2(monstruo3)
            if usuario.vidaActual > 0:
                usuario.vidaActual+=2
            elif usuario.vidaActual==0:
                dialogoDefeat()
                break
            if monstruo3.vidaActual==0:
                dialogoWin(monstruo3,monedas3,expe3)
                break
            recuperarVida()
        elif (accion=="b" or accion=="B") and aleatorio==3:
            comanComand2(monstruo4)
            if usuario.vidaActual > 0:
                usuario.vidaActual+=2
            elif usuario.vidaActual==0:
                dialogoDefeat()
                break
            if monstruo4.vidaActual==0:
                dialogoWin(monstruo4.nombre,monedas4,expe4)
                break
            recuperarVida()
        elif accion=="v":
            os.system("cls")
            break
        else:
            charlantina()
            continue

def releccion() -> None:
    print("posibles enemigos:")
    print(f"mapa: \"Bosque Sombrio\"{enemigos[0]}")
    print(f"mapa: \"Desierto Arido\"{enemigos[1]}")
    os.system("echo.")
    os.system("echo.")

def combate() -> None:
    while True:
        title("MAPAS","nombre","mapas")
        os.system("echo.")
        print("Bosque Sombrio")
        print("Desieto Arido")
        os.system("echo.")
        os.system("echo.")
        seleccion=input("seleccione el mapa:")
        if seleccion=="bosque sombrio":
            os.system("cls")
            mapas(Goblin,10,40,Goblin5,35,100,Esqueleto,20,70,Esqueleto5,50,150,1)
            nivel()
            releccion()
            inp=input("si desea buscar otro oponnete ingese 1, sino presione cualquier tecla:")
            if inp=="1":
                os.system("cls")
                restaurar()
                continue
            else:
                os.system("cls")
                break
        elif seleccion=="desierto arido":
            os.system("cls")
            mapas(Escorpion,20,70,Escorpion5,50,200,Minotauro,40,120,Minotauro5,150,350,2)
            nivel()
            releccion()
            inp=input("si desea buscar otro oponnete ingese 1, sino presione cualquier tecla:")
            if inp=="1":
                os.system("cls")
                restaurar()
                continue
            else:
                os.system("cls")
                break
        elif seleccion=="salir":
            os.system("cls")
            break
        else:
            charlantina()
            continue
        

def critico1(monstuo:mobs) -> None:
    valor=random.randint(0,3)
    monstuo.vidaActual-=valor
    print("CRITICO ---> +"+str(valor))

def critico2(monstuo:mobs) -> None:
    valor=random.randint(1,4)
    monstuo.vidaActual-=valor
    print("CRITICO ---> +"+str(valor))

def critico3(monstuo:mobs) -> None:
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


def estadoJugador() -> None:
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


def moneditasIn() -> None:
    os.system("cls")
    print("monedas insuficientes!!")
    print("seleccione un objeto que pueda comprar")
    os.system("echo.")

def storeComan(arma: 'arma',monedas:int) -> None:
    mochila.append(arma.nombreArma)
    usuario.monedas-=monedas
    os.system("cls")
    print(f"{arma.nombreArma} comprada con exito!")
    print(f"monedas -{monedas}")
    os.system("echo.")

def title(opcion:str, piplo:str, piplo2:str) -> None:
    print(f"***************************{opcion}***************************")
    estadoJugador()

    print(f"Seleccione el {piplo} del {piplo2} que quiere comprar:")
    print("para volver presione \"SALIR\"")
    os.system("echo.")

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
                title("ARMADURAS","ID","objetos")

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
                        moneditasIn()
                        continue
                    mochila1.append(cascoCuero.nombreArmadura)
                    usuario.monedas-=30
                    os.system("cls")
                elif accion=="salir":
                    os.system("cls")
                    break
                elif accion=="ch_cu":
                    if usuario.monedas < 50:
                        moneditasIn()
                        continue
                    mochila1.append(chalecoCuero.nombreArmadura)
                    usuario.monedas-=50
                    os.system("cls")
                elif accion=="p_cu":
                    if usuario.monedas < 40:
                        moneditasIn()
                        continue
                    mochila1.append(piernasCuero.nombreArmadura)
                    usuario.monedas-=40
                    os.system("cls")
                elif accion=="b_cu":
                    if usuario.monedas <30:
                        moneditasIn()
                        continue
                    mochila1.append(botasCuero.nombreArmadura)
                    usuario.monedas-=30
                    os.system("cls")
                elif accion=="s_ir":
                    if usuario.monedas < 50:
                        moneditasIn()
                        continue
                    mochila1.append(escudoHierro.nombreArmadura)
                    usuario.monedas-=50
                    os.system("cls")
                else:
                    charlantina()
                    os.system("echo.")

        elif eleccion=="armas":
            os.system("cls")
            while True:
                title("ARMAS","ID","objetos")

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
                        moneditasIn()
                        continue
                    storeComan(espada,30)
                elif accion=="salir":
                    os.system("cls")
                    break
                elif accion=="arc":
                    if usuario.monedas < 50:
                        moneditasIn()
                        continue
                    storeComan(arco,50)
                elif accion=="ach":
                    if usuario.monedas < 75:
                        moneditasIn()
                        continue
                    storeComan(hacha,75)
                elif accion=="ktn":
                    if usuario.monedas < 150:
                        moneditasIn()
                        continue
                    storeComan(katana,150)
                elif accion=="mrt":
                    if usuario.monedas < 250:
                        moneditasIn()
                        continue
                    storeComan(martillo,250)
                elif accion=="smw":
                    if usuario.monedas < 600:
                        moneditasIn()
                        continue
                    storeComan(samrtSword,600)
                else:
                    charlantina()
                    os.system("echo.")
        elif eleccion=="pot":
            while True:
                os.system("cls")
                title("POCIONEs","ID","objetos")
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
            charlantina()
            continue

def comanBag(arma: 'arma',coman:int) -> None:
    if coman==1:
        usuario.ARMA=arma
        mochila.append(arma.nombreArma)
        os.system("cls")
    elif coman==2:
        usuario.ARMA=arma
        mochila.remove(arma.nombreArma)
        os.system("cls")


def Mochila():
    while True:
        print("Para desequipar presione \"D\"")
        print("Para equipar presione \"E\"")
        print("para volver presione \"V\"")

        print(f"ARMAS: {mochila}")
        print(f"ARMADURAS: {mochila1}")

        opcion=input("Elija una opcion:")

        if opcion=="d":
            os.system("cls")
            while True:
                print("para salir esciba \"SALIR\"")
                os.system("echo.")
                print("nombre del objeto a desequipar:")
                print("arma equipada: ["+usuario.ARMA.nombreArma+"]")
                print("casco equipado: ["+usuario.casco.nombreArmadura+"]")
                print("chaleco equipada: ["+usuario.pecho.nombreArmadura+"]")
                print("piernas equipada: ["+usuario.piernas.nombreArmadura+"]")
                print("pies equipado: ["+usuario.pies.nombreArmadura+"]")
                print("escudo equipado: ["+usuario.escudo.nombreArmadura+"]")
                os.system("echo.")
                opcion1=input("nombre:")
                if opcion1== "espada":
                    if usuario.ARMA==vacio or usuario.ARMA != espada:
                        charlantina()
                        continue
                    comanBag(espada,1)
                elif opcion1=="arco":
                    if usuario.ARMA==vacio or usuario.ARMA != arco:
                        charlantina()
                        continue
                    comanBag(arco,1)
                elif opcion1=="hacha":
                    if usuario.ARMA==vacio or usuario.ARMA != hacha:
                        charlantina()
                        continue
                    comanBag(hacha,1)
                elif opcion1=="katana":
                    if usuario.ARMA==vacio or usuario.ARMA != katana:
                        charlantina()
                        continue
                    comanBag(katana,1)
                elif opcion1=="martillo":
                    if usuario.ARMA==vacio or usuario.ARMA != martillo:
                        charlantina()
                        continue
                    comanBag(martillo,1)
                elif opcion1=="esapda-inteligente":
                    if usuario.ARMA==vacio or usuario.ARMA != samrtSword:
                        charlantina()
                        continue
                    comanBag(samrtSword,1)
                elif usuario.ARMA==vacio:
                    os.system("cls")
                    print("ya esta vacio el lote!!")
                    continue
                elif opcion1=="casco de cuero":
                    if usuario.vacia==vacio or usuario.ARMA != cascoCuero:
                        charlantina()
                        continue
                    usuario.casco=cascoCuero
                    mochila1.append(cascoCuero.nombreArmadura)
                    os.system("cls")
                elif opcion1=="chaleco de cuero":
                    if usuario.ARMA==vacia or usuario.ARMA != chalecoCuero:
                        charlantina()
                        continue
                    usuario.pecho=chalecoCuero
                    mochila1.append(chalecoCuero.nombreArmadura)
                    os.system("cls")
                elif opcion1=="piernas de cuero":
                    if usuario.ARMA==vacia or usuario.ARMA != piernasCuero:
                        charlantina()
                        continue
                    usuario.piernas=piernasCuero
                    mochila1.append(piernasCuero.nombreArmadura)
                    os.system("cls")
                elif opcion1=="botas de cuero":
                    if usuario.ARMA==vacia or usuario.ARMA != botasCuero:
                        charlantina()
                        continue
                    usuario.pies=botasCuero
                    mochila1.append(botasCuero.nombreArmadura)
                    os.system("cls")
                elif opcion1=="escudo de hierro":
                    if usuario.ARMA==vacia or usuario.ARMA != escudoHierro:
                        charlantina()
                        continue
                    usuario.escudo=escudoHierro
                    mochila.append(escudoHierro.nombreArmadura)
                    os.system("cls")
                elif opcion1=="salir":
                    os.system("cls")
                    break
                else:
                    charlantina()
                    continue
        elif opcion=="e":
            os.system("cls")
            while True:
                print("para salir esciba \"SALIR\"")
                print("para equipar armadura escriba\"ARMADURA\"")
                print("para equipar arma escriba\"ARMA\"")

                print(f"ARMAS: {mochila}")
                print(f"ARMADURAS: {mochila1}")

                definir=input("seleccion su opcion:")
                
                if definir=="arma":
                    os.system("cls")
                    while True:
                        print("para salir esciba \"SALIR\"")
                        if usuario.ARMA != vacio:
                            mochila.append(usuario.ARMA.nombreArma)
                            usuario.ARMA=vacio
                        print(f"ARMAS:{mochila}")
                        os.system("echo.")
                        opcion2=input("nombre del objeto a equipar:")
                        if opcion2== "espada":
                            if espada.nombreArma not in mochila:
                                charlantina()
                                continue
                            comanBag(espada,2)
                        elif opcion2=="arco":
                            if arco.nombreArma not in mochila:
                                charlantina()
                                continue
                            comanBag(arco,2)
                        elif opcion2=="hacha":
                            if hacha.nombreArma not in mochila:
                                charlantina()
                                continue
                            comanBag(hacha,2)
                        elif opcion2=="katana":
                            if katana.nombreArma not in mochila:
                                charlantina()
                                continue
                            comanBag(katana,2)
                        elif opcion2=="martillo":
                            if martillo.nombreArma not in mochila:
                                charlantina()
                                continue
                            comanBag(martillo,2)
                        elif opcion2=="esapda_inteligente":
                            if samrtSword.nombreArma not in mochila:
                                charlantina()
                                continue
                            comanBag(samrtSword,2)
                        elif opcion2=="salir":
                            os.system("cls")
                            break
                        else:
                            charlantina()
                            continue
                elif definir=="armadura":
                    os.system("cls")
                    while True:
                        print("para salir esciba \"SALIR\"")
                        print(f"ARMADURAS:{mochila1}")
                        os.system("echo.")
                        opcion2=input("nombre del objeto a equipar:")
                        if opcion2== "casco de cuero":
                            if usuario.casco != vacia:
                                mochila1.append(usuario.casco.nombreArmadura)
                                usuario.ARMA=vacia
                            if cascoCuero.nombreArmadura not in mochila1:
                                charlantina()
                                continue
                            usuario.casco=cascoCuero
                            mochila1.remove(cascoCuero.nombreArmadura)
                            os.system("cls")
                        elif opcion2=="chaleco de cuero":
                            if usuario.pecho != vacia:
                                mochila1.append(usuario.pecho.nombreArmadura)
                                usuario.pecho=vacia
                            if chalecoCuero.nombreArmadura not in mochila1:
                                charlantina()
                                continue
                            usuario.pecho=chalecoCuero
                            mochila1.remove(chalecoCuero.nombreArmadura)
                            os.system("cls")
                        elif opcion2=="pantalon de cuero":
                            if usuario.piernas != vacia:
                                mochila1.append(usuario.piernas.nombreArmadura)
                                usuario.piernas=vacia
                            if piernasCuero.nombreArmadura not in mochila1:
                                charlantina()
                                continue
                            usuario.piernas=piernasCuero
                            mochila1.remove(piernasCuero.nombreArmadura)
                            os.system("cls")
                        elif opcion2=="botas de cuero":
                            if usuario.pies != vacia:
                                mochila1.append(usuario.pies.nombreArmadura)
                            usuario.ARMA=vacia
                            if botasCuero.nombreArmadura not in mochila1:
                                charlantina()
                                continue
                            usuario.pies=botasCuero
                            mochila1.remove(botasCuero.nombreArmadura)
                            os.system("cls")
                        elif opcion2=="escudo de hierro":
                            if escudoHierro.nombreArmadura not in mochila1:
                                charlantina()
                                continue
                            usuario.escudo=escudoHierro
                            mochila1.remove(escudoHierro.nombreArmadura)
                            os.system("cls")
                        elif opcion2=="salir":
                            os.system("cls")
                            break
                        else:
                            charlantina()
                            continue
                elif definir=="salir":
                    os.system("cls")
                    break
                else:
                    charlantina()
                    continue
        elif opcion=="v":
            os.system("cls")
            break
        else:
            charlantina()
            continue

def comanLevel(nivelote,vidamaxima,ataquebase,aumentovida):
    if usuario.experiencia>=(10**nivelote)/2 and usuario.experiencia<(10**(nivelote+1))/2:
        usuario.experiencia=0
        usuario.nivel=nivelote
        usuario.vidaMaxima=vidamaxima
        usuario.vidaActual=usuario.vidaMaxima
        usuario.ataqueBase+=ataquebase
        print(f" ¡¡FELICIDADES HAS SUBIDO AL NIVEL \"{nivelote}\"!!")
        os.system("echo.")
        print("*****BONUS DE NIVEL*****")
        print(f"-vida maxima: +{aumentovida}")
        print(f"-ataque base: +{ataquebase}")
        os.system("echo.")

def nivel():
    if usuario.nivel==1:
        comanLevel(2,22,1,2)
    elif usuario.nivel==2:
        comanLevel(3,25,2,3)
    elif usuario.nivel==3:
        comanLevel(4,27,3,2)
    elif usuario.nivel==4:
        comanLevel(5,30,4,3)

def restaurar():
    Goblin.vidaActual=Goblin.vidaMaxima
    Goblin5.vidaActual=Goblin5.vidaMaxima
    Esqueleto.vidaActual=Esqueleto.vidaMaxima
    Esqueleto5.vidaActual=Esqueleto5.vidaMaxima
    usuario.vidaActual=usuario.vidaMaxima

def main() -> None:
    while True:

        while True:
            restaurar()
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
                charlantina()
                break
    
if __name__=='__main__':
    main()
