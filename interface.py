#-*- coding: utf-8 -*-

from monstruo import *
import os,random
import time as tm
from progress.bar import Bar
from animation import *


mochilaClases=["mago","arquero","guerrero","berserker"]
Lista=[]
Lista1=[]
listapam=["si"]
listapam1=["si"]
listaparm2=["si"]
dropp=[]

usuario=Jugador(20,arcoPlatinado,"",vacia,vacia,vacia,botasCuero,vacia)


def charlantina() -> None:
    os.system("cls")
    print("OPCION INVALIDA!!")
    print("por favor, ingrese una opcion valida.")
    os.system("echo.")


def guardadoCarpeta(nombre: str,sector: str,parametro: str, n: str) -> None:
    
    lista=os.listdir("./")

    if nombre not in lista:
        os.makedirs(nombre)

    loc=f"{nombre}/{sector}"

    if n=="1":
        with open(loc, 'w+') as f:
            f.write(parametro)
            f.close()
    elif n=="2":
        with open(loc, 'w') as f:
            f.write(parametro)
            f.close()
    elif n=="3":
        global mostrar
        with open(loc) as f:
            mostrar=f.read()
            f.close()


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


def mod() -> None:
    print("CLASES:")
    print(mochilaClases)
    stats(cascoCuero,vacia,vacia,vacia,vacia,"MAGO",18,cetroMagico.nombreArma,4,0)
    stats(vacia,vacia,vacia,vacia,vacia,"GUERRERO",22,espadaHierro.nombreArma,0,2)
    stats(vacia,vacia,vacia,botasCuero,vacia,"ARQUERO",20,arcoPlatinado.nombreArma,1,1)
    stats(vacia,vacia,vacia,vacia,vacia,"BERSERKER",22,hacha.nombreArma,2,0)


def login() -> None:
    global nombreUsuario
    global m
    os.system("cls")
    print("-------------------------BIENVENIDO-------------------------\n")
    print("si desea iniciar sesion escriba \"LOG\"\nsino presione enter.\n")
    print("para cerrar el programa escriba \"SALIR\"\n")
    opcion=input("ingrese una opcion:")
    os.system("cls")

    if opcion=="log" or opcion=="LOG":
        lista=os.listdir("./")
        print("------------------------INICIO DE SESION-------------------------\n")
        nombre=input("nombre de Usuario:")
        if nombre not in lista:
            charlantina()
            print("USAURIO NO REGISTRADO!")
            tm.sleep(1.0)
            login()
        if nombre in lista:
            m="3"
            guardadoCarpeta(nombre,"monedas","nada",m)
            usuario.monedas=int(mostrar)
            guardadoCarpeta(nombre,"Diamantes","nada",m)
            usuario.diamantes=int(mostrar)
            guardadoCarpeta(nombre,"Amatistas","nada",m)
            usuario.amatistas=int(mostrar)
            guardadoCarpeta(nombre,"nombre","nada",m)
            usuario.nombre=mostrar
            guardadoCarpeta(nombre,"experiencia","nada",m)
            usuario.experiencia=int(mostrar)
            guardadoCarpeta(nombre,"nivel","nada",m)
            usuario.nivel=int(mostrar)
            guardadoCarpeta(nombre,"vidamaxima","nada",m)
            usuario.vidaMaxima=int(mostrar)
            guardadoCarpeta(nombre,"ataquebase","nada",m)
            usuario.ataqueBase=int(mostrar)
            guardadoCarpeta(nombre,"defensabase","nada",m)
            usuario.defensaBase=int(mostrar)
            guardadoCarpeta(nombre,"arma","nada",m)
            if mostrar=="<class 'monstruo.espada'>":
                usuario.ARMA=espada
            if mostrar=="<class 'monstruo.arco'>":
                usuario.ARMA=arco
            if mostrar=="<class 'monstruo.hacha'>":
                usuario.ARMA=hacha
            if mostrar=="<class 'monstruo.cetroMagico'>":
                usuario.ARMA=cetroMagico
            if mostrar=="<class 'monstruo.espadaHierro'>":
                usuario.ARMA=espadaHierro
            if mostrar=="<class 'monstruo.arcoPlatinado'>":
                usuario.ARMA=arcoPlatinado
            if mostrar=="<class 'monstruo.katana'>":
                usuario.ARMA=katana
            if mostrar=="<class 'monstruo.martillo'>":
                usuario.ARMA=martillo
            if mostrar=="<class 'monstruo.samrtSword'>":
                usuario.ARMA=samrtSword
            if mostrar=="<class 'monstruo.vacio'>":
                usuario.ARMA=vacio
            guardadoCarpeta(nombre,"casco","nada",m)
            if mostrar=="<class 'monstruo.cascoCuero'>":
                usuario.casco=cascoCuero
            if mostrar=="<class 'monstruo.vacia'>":
                usuario.casco=vacia
            guardadoCarpeta(nombre,"pecho","nada",m)
            if mostrar=="<class 'monstruo.chalecoCuero'>":
                usuario.pecho=chalecoCuero
            if mostrar=="<class 'monstruo.vacia'>":
                usuario.pecho=vacia
            guardadoCarpeta(nombre,"piernas","nada",m)
            if mostrar=="<class 'monstruo.piernasCuero'>":
                usuario.piernas=piernasCuero
            if mostrar=="<class 'monstruo.vacia'>":
                usuario.piernas=vacia
            guardadoCarpeta(nombre,"botas","nada",m)
            if mostrar=="<class 'monstruo.botasCuero'>":
                usuario.pies=botasCuero
            if mostrar=="<class 'monstruo.vacia'>":
                usuario.pies=vacia
            guardadoCarpeta(nombre,"escudo","nada",m)
            if mostrar=="<class 'monstruo.escudoHierro'>":
                usuario.escudo=escudoHierro
            if mostrar=="<class 'monstruo.vacia'>":
                usuario.escudo=vacia
            guardadoCarpeta(nombre,"critico","nada",m)
            usuario.critico=int(mostrar)
            guardadoCarpeta(nombre,"clase","nada",m)
            usuario.clase=mostrar
            m="2"
            barrita('CARGANDO')
            os.system("cls")
    elif opcion=="salir" or opcion=="SALIR":
        exit()
    elif opcion=="":
        os.system("cls")
        nombreUsuario=input("ingrese su nombre de Usuario:")
        m="1"
        barrita('INGRESANDO')
        os.system("cls")
    else:
        charlantina()
        tm.sleep(1.0)
        login()


def barrita(parametro: str) -> None:
    bar1=Bar(parametro,max=100)
    for i in range(100):
        tm.sleep(0.05)
        bar1.next()
    bar1.finish()
    

login()
if m=="1":
    mod()

while True:

    if m=="2":
        break

    clase=input("elija la clase de su personaje:")

    if clase=="mago" or clase=="MAGO": 
        usuario.vidaMaxima=18
        usuario.ARMA=cetroMagico
        usuario.nombre=nombreUsuario
        usuario.casco=cascoCuero
        usuario.pecho=vacia
        usuario.piernas=vacia
        usuario.pies=vacia
        usuario.escudo=vacia
        usuario.ataqueBase=4
        usuario.clase="mago"
        os.system("cls")
        break

    elif clase=="guerrero" or clase=="GUERRERO":
        usuario.vidaMaxima=22
        usuario.ARMA=espadaHierro
        usuario.nombre=nombreUsuario
        usuario.casco=vacia
        usuario.pecho=vacia
        usuario.piernas=vacia
        usuario.pies=vacia
        usuario.escudo=vacia
        usuario.defensaBase=2
        usuario.clase="guerrero"
        os.system("cls")
        break

    elif clase=="arquero" or clase=="ARQUERO":
        usuario.vidaMaxima=20
        usuario.ARMA=arcoPlatinado
        usuario.nombre=nombreUsuario
        usuario.casco=vacia
        usuario.pecho=vacia
        usuario.piernas=vacia
        usuario.pies=botasCuero
        usuario.escudo=vacia
        usuario.defensaBase=1
        usuario.ataqueBase=1
        usuario.clase="arquero"
        os.system("cls")
        break

    elif clase=="berserker" or clase=="BERSERKER":
        usuario.vidaMaxima=22
        usuario.ARMA=cetroMagico
        usuario.nombre=nombreUsuario
        usuario.casco=vacia
        usuario.pecho=vacia
        usuario.piernas=vacia
        usuario.pies=vacia
        usuario.escudo=vacia
        usuario.ataqueBase=2
        usuario.clase="berserker"
        os.system("cls")
        break

    else:
        charlantina()
        os.system("echo.")
        mod()
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


def drop(monstruo: 'mobs',monstruo2: 'mobs',num: int,num1: int, num2: int) -> None:
    if monstruo==monstruo2:
        ran=random.randint(0,num)
        if ran==10:
            usuario.diamantes+=num1
            print(f"diamantes +{num1}")
        elif ran==20:
            usuario.diamante+=num2
            print(f"diamantes +{num2}")
        elif ran==85:
            usuario.amatistas+=num1
            print(f"amatistas +{num1}")
        elif ran==1:
            usuario.amatsitas+=num2
            print(f"amatistas +{num2}")


def comanCobat(monstruo: 'mobs',monedas: int,exp: int) -> None:

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
    if usuario.vidaActual==0:
        dialogoDefeat()
        listapam[0]="no"
    elif monstruo.vidaActual==0:
        dialogoWin(monstruo,monedas,exp)
        listapam[0]="no"
    recuperarVida()

def comanComand2(monstruo: 'mobs',monedas: int,exp: int) -> None:

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

    if usuario.vidaActual > 0:
        usuario.vidaActual+=2
    elif usuario.vidaActual==0:
        dialogoDefeat()
        listapam[0]="no"
    if monstruo.vidaActual==0:
        dialogoWin(monstruo,monedas,exp)
        listapam[0]="no"

def dialogoDefeat() -> None:

    print("¡¡PERDISTE!!")
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR...")
    os.system("cls")

def dialogoWin(palabrin: 'mobs',monedas:int,exp:int) -> None:

    print(f"MATASTE A {palabrin.nombre}!")
    print(f"+{monedas} monedas")
    usuario.monedas+=monedas
    print(f"+{exp} EXP")
    usuario.experiencia+=exp
    drop(palabrin,Goblin,200,2,5)
    drop(palabrin,Goblin5,150,5,7)
    drop(palabrin,Esqueleto,175,3,5)
    drop(palabrin,Esqueleto5,125,7,8)
    drop(palabrin,Escorpion,150,5,6)
    drop(palabrin,Escorpion5,115,10,12)
    drop(palabrin,Minotauro,125,12,15)
    drop(palabrin,Minotauro5,100,20,25)
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

    aleatorio=random.randint(0,3)

    while listapam[0]=="si":

        estadoJugador()
        
        seleccion(aleatorio,divicion)

        print("para atacar preisone\"A\"")
        os.system("echo.")
        print("para defenderse preisone\"B\"")
        os.system("echo.")
        print("para volver presione \"V\"")
        accion=input("ingrese una opcion:")

        if (accion=="a" or accion=="A") and aleatorio==0:
            comanCobat(monstruo1,monedas1,expe1)
        elif (accion=="a" or accion=="A") and aleatorio==1:
            comanCobat(monstruo2,monedas2,expe2)
        elif (accion=="a" or accion=="A") and aleatorio==2:
            comanCobat(monstruo3,monedas3,expe3)
        elif (accion=="a" or accion=="A") and aleatorio==3:
            comanCobat(monstruo4,monedas4,expe4)
        elif (accion=="b" or accion=="B") and aleatorio==0:
            comanComand2(monstruo1,monedas1,expe1)
        elif (accion=="b" or accion=="B") and aleatorio==1:
            comanComand2(monstruo2,monedas2,expe2)
        elif (accion=="B" or accion=="b") and aleatorio==2:
            comanComand2(monstruo3,monedas3,expe3)
        elif (accion=="b" or accion=="B") and aleatorio==3:
            comanComand2(monstruo4,monedas4,expe4)
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

def rellcombate(m1,mon1,exp1,m2,mon2,exp2,m3,mon3,exp3,m4,mon4,exp4,num):

    listapam[0]="si"
    os.system("cls")
    mapas(m1,mon1,exp1,m2,mon2,exp2,m3,mon3,exp3,m4,mon4,exp4,num)
    nivel()
    releccion()
    inp=input("si desea buscar otro oponnete ingese 1, sino presione cualquier tecla:")
    if inp=="1":
        os.system("cls")
        restaurar()
        combate()
    else:
        os.system("cls")
        listapam1[0]="no"

def combate() -> None:
    while listapam1[0]=="si":
        title("MAPAS","nombre","mapas")
        os.system("echo.")
        print("Bosque Sombrio")
        print("Desieto Arido")
        os.system("echo.")
        os.system("echo.")
        seleccion=input("seleccione el mapa:")
        if seleccion=="bosque sombrio":
            rellcombate(Goblin,10,40,Goblin5,35,100,Esqueleto,20,70,Esqueleto5,50,150,1)
        elif seleccion=="desierto arido":
            rellcombate(Escorpion,20,70,Escorpion5,50,200,Minotauro,40,120,Minotauro5,150,350,2)
        elif seleccion=="salir":
            os.system("cls")
            listapam1[0]="no"
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
    print(f"Nombre de Usuario: {usuario.nombre}    Arma actual: {usuario.ARMA.nombreArma}       Monedas: {usuario.monedas}")
    print(f"CLASE: {usuario.clase}                   casco: {usuario.casco.nombreArmadura}    Diamantes: {usuario.diamantes}")
    print(f"Vida actual: {usuario.vidaActual}               pecho:{usuario.pecho.nombreArmadura}              Amatistas: {usuario.amatistas}")
    print("EXP: "+str(usuario.experiencia)+"/"+str((10**(usuario.nivel+1)/2))+f"                   piernas:{usuario.piernas.nombreArmadura}")
    print(f"NIVEL: {usuario.nivel}                      pies:{usuario.pies.nombreArmadura}")
    print(f"                              escudo:{usuario.escudo.nombreArmadura}")
    print(f"                              ")
    print(f"                                                                            ")
    print(f"                                                                            ")
    print(f"                                                                            ")
    print(f"                                                                            ")
    print(f"                                                                            ")


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

def rellTienda(mon, parm) -> None:
    if usuario.monedas < mon:
        moneditasIn()
        tienda()
    mochila1.append(parm.nombreArmadura)
    usuario.monedas-=mon
    os.system("cls")

def rellTienda2(mon,parm):
    if usuario.monedas < mon:
        moneditasIn()
        tienda()
    storeComan(parm,mon)

def tienda() -> None:
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
                    rellTienda(30,cascoCuero)
                elif accion=="salir":
                    os.system("cls")
                    break
                elif accion=="ch_cu":
                    rellTienda(50,chalecoCuero)
                elif accion=="p_cu":
                    rellTienda(40,piernasCuero)
                elif accion=="b_cu":
                    rellTienda(30,botasCuero)
                elif accion=="s_ir":
                    rellTienda(50,escudoHierro)
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
                print("ID: ctr (cetro) ---> precio 75 monedas.")
                print("ID: esp_h (esapada de hierro) ---> precio 75 monedas.")
                print("ID: arc_p (arco platinado) ---> precio 75 monedas.")
                print("ID: ktn (katana) ---> precio 150 monedas.")
                print("ID: mrt (martillo) ---> precio 250 monedas.")
                print("ID: smw (espada intelgente) ---> precio 600 monedas.")
                os.system("echo.")

                print(mochila)
                os.system("echo.")

                accion=input("elija una opcion:")

                if accion=="esp":
                    rellTienda2(30,espada)
                elif accion=="salir":
                    os.system("cls")
                    break
                elif accion=="arc":
                    rellTienda2(50,arco)
                elif accion=="ach":
                    rellTienda2(75,hacha)
                elif accion=="esp_h":
                    rellTienda2(75,espadaHierro)
                elif accion=="ctr":
                    rellTienda2(75,cetroMagico)
                elif accion=="arc_p":
                    rellTienda2(75,arcoPlatinado)
                elif accion=="ktn":
                    rellTienda2(150,katana)
                elif accion=="mrt":
                    rellTienda2(250,martillo)
                elif accion=="smw":
                    rellTienda2(600,samrtSword)
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
        usuario.ARMA=vacio
        mochila.append(arma.nombreArma)
        os.system("cls")
    elif coman==2:
        usuario.ARMA=arma
        mochila.remove(arma.nombreArma)
        os.system("cls")

def rellMochila(parm: 'arma', num: int) -> None:
    if usuario.ARMA==vacio or usuario.ARMA != parm:
        charlantina()
        Mochila()
    comanBag(parm,num)

def rellMochila2(parm2: 'armadura',num: int):
    
    if num==1:        
        if usuario.casco==vacia or usuario.casco != parm2:
            charlantina()
            Mochila()
        usuario.casco=vacia
        mochila1.append(parm2.nombreArmadura)
        os.system("cls")
    elif num==2:
        if usuario.pecho==vacia or usuario.pecho != parm2:
            charlantina()
            Mochila()
        usuario.pecho=vacia
        mochila1.append(parm2.nombreArmadura)
        os.system("cls")
    elif num==3:
        if usuario.piernas==vacia or usuario.piernas != parm2:
            charlantina()
            Mochila()
        usuario.piernas=vacia
        mochila1.append(parm2.nombreArmadura)
        os.system("cls")
    elif num==4:
        if usuario.pies==vacia or usuario.pies != parm2:
            charlantina()
            Mochila()
        usuario.pies=vacia
        mochila1.append(parm2.nombreArmadura)
        os.system("cls")
    elif num==5:
        if usuario.escudo==vacia or usuario.escudo != parm2:
            charlantina()
            Mochila()
        usuario.escudo=vacia
        mochila1.append(parm2.nombreArmadura)
        os.system("cls")

def rellMochila3(parm: 'arma',num):
    if parm.nombreArma not in mochila:
        charlantina()
        Mochila()
    else:
        comanBag(parm,num)
        listaparm2[0]="no"

def rellMochila4(num,parm2: 'armadura'):
        
    if num==1:
        if usuario.casco != vacia:
            mochila1.append(usuario.casco.nombreArmadura)
        if parm2.nombreArmadura not in mochila1:
            charlantina()
            Mochila()
        usuario.casco=parm2
        mochila1.remove(parm2.nombreArmadura)
        os.system("cls")
    elif num==2:
        if usuario.pecho != vacia:
            mochila1.append(usuario.pecho.nombreArmadura)
        if parm2.nombreArmadura not in mochila1:
            charlantina()
            Mochila()
        usuario.pecho=parm2
        mochila1.remove(parm2.nombreArmadura)
        os.system("cls")
    elif num==3:
        if usuario.piernas != vacia:
            mochila1.append(usuario.piernas.nombreArmadura)
        if parm2.nombreArmadura not in mochila1:
            charlantina()
            Mochila()
        usuario.piernas=parm2
        mochila1.remove(parm2.nombreArmadura)
        os.system("cls")
    elif num==4:
        if usuario.pies != vacia:
            mochila1.append(usuario.pies.nombreArmadura)
        if parm2.nombreArmadura not in mochila1:
            charlantina()
            Mochila()
        usuario.pies=parm2
        mochila1.remove(parm2.nombreArmadura)
        os.system("cls")
    elif num==5:
        if usuario.escudo != vacia:
            mochila1.append(usuario.escudo.nombreArmadura)
        if parm2.nombreArmadura not in mochila1:
            charlantina()
            Mochila()
        usuario.escudo=parm2
        mochila1.remove(parm2.nombreArmadura)
        os.system("cls")

def Mochila() -> None:
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
                    rellMochila(espada,1)
                elif opcion1=="arco":
                    rellMochila(arco,1)
                elif opcion1=="hacha":
                    rellMochila(hacha,1)
                elif opcion1=="espada de hierro":
                    rellMochila(espadaHierro,1)
                elif opcion1=="cetro":
                    rellMochila(cetroMagico,1)
                elif opcion1=="arco platinado":
                    rellMochila(arcoPlatinado,1)
                elif opcion1=="katana":
                    rellMochila(katana,1)
                elif opcion1=="martillo":
                    rellMochila(martillo,1)
                elif opcion1=="esapda-inteligente":
                    rellMochila(samrtSword,1)
                elif opcion1=="casco de cuero":
                    rellMochila2(cascoCuero,1)
                elif opcion1=="chaleco de cuero":
                    rellMochila2(chalecoCuero,2)
                elif opcion1=="piernas de cuero":
                    rellMochila2(piernasCuero,3)
                elif opcion1=="botas de cuero":
                    rellMochila2(botasCuero,4)
                elif opcion1=="escudo de hierro":
                    rellMochila2(escudoHierro,5)
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
                    while listaparm2[0]=="si":
                        print("para salir esciba \"SALIR\"")
                        if usuario.ARMA != vacio:
                            mochila.append(usuario.ARMA.nombreArma)
                            usuario.ARMA=vacio
                        print(f"ARMAS:{mochila}")
                        os.system("echo.")
                        opcion2=input("nombre del objeto a equipar:")
                        if opcion2== "espada":
                            rellMochila3(espada,2)
                        elif opcion2=="arco":
                            rellMochila3(arco,2)
                        elif opcion2=="hacha":
                            rellMochila3(hacha,2)
                        elif opcion2=="arco platinado":
                            rellMochila3(arcoPlatinado,2)
                        elif opcion2=="espada de hierro":
                            rellMochila3(espadaHierro,2)
                        elif opcion2=="cetro":
                            rellMochila3(cetroMagico,2)
                        elif opcion2=="katana":
                            rellMochila3(katana,2)
                        elif opcion2=="martillo":
                            rellMochila3(martillo,2)
                        elif opcion2=="esapda_inteligente":
                            rellMochila3(samrtSword,2)
                        elif opcion2=="salir":
                            os.system("cls")
                            listaparm2[0]="no"
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
                            rellMochila4(1,cascoCuero)
                        elif opcion2=="chaleco de cuero":
                            rellMochila4(2,chalecoCuero)
                        elif opcion2=="pantalon de cuero":
                            rellMochila4(3,piernasCuero)
                        elif opcion2=="botas de cuero":
                            rellMochila4(4,botasCuero)
                        elif opcion2=="escudo de hierro":
                            rellMochila4(5,escudoHierro)
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

def comanLevel(nivel,nivelote,ataquebase,aumentovida)-> None:

    if usuario.nivel==nivel:
        if usuario.experiencia>=(10**nivelote)/2 and usuario.experiencia<(10**(nivelote+1))/2:
            usuario.experiencia=0
            usuario.nivel=nivelote
            usuario.vidaMaxima+=aumentovida
            usuario.vidaActual=usuario.vidaMaxima
            usuario.ataqueBase+=ataquebase
            print(f" ¡¡FELICIDADES HAS SUBIDO AL NIVEL \"{nivelote}\"!!")
            os.system("echo.")
            print("*****BONUS DE NIVEL*****")
            print(f"-vida maxima: +{aumentovida}")
            print(f"-ataque base: +{ataquebase}")
            os.system("echo.")

def nivel() -> None:

    comanLevel(1,2,1,2)
    comanLevel(2,3,2,3)
    comanLevel(3,4,3,2)
    comanLevel(4,5,4,3)
    comanLevel(5,6,1,2)
    comanLevel(6,7,1,2)

def restaurar() -> None:
    Goblin.vidaActual=Goblin.vidaMaxima
    Goblin5.vidaActual=Goblin5.vidaMaxima
    Esqueleto.vidaActual=Esqueleto.vidaMaxima
    Esqueleto5.vidaActual=Esqueleto5.vidaMaxima
    usuario.vidaActual=usuario.vidaMaxima

def reg(nombreUsuario,n):
    guardadoCarpeta(nombreUsuario,"monedas",str(usuario.monedas),n)
    guardadoCarpeta(nombreUsuario,"nombre",str(nombreUsuario),n)
    guardadoCarpeta(nombreUsuario,"experiencia",str(usuario.experiencia),n)
    guardadoCarpeta(nombreUsuario,"nivel",str(usuario.nivel),n)
    guardadoCarpeta(nombreUsuario,"vidamaxima",str(usuario.vidaMaxima),n)
    guardadoCarpeta(nombreUsuario,"ataquebase",str(usuario.ataqueBase),n)
    guardadoCarpeta(nombreUsuario,"defensabase",str(usuario.defensaBase),n)
    guardadoCarpeta(nombreUsuario,"arma",str(usuario.ARMA),n)
    guardadoCarpeta(nombreUsuario,"casco",str(usuario.casco),n)
    guardadoCarpeta(nombreUsuario,"pecho",str(usuario.pecho),n)
    guardadoCarpeta(nombreUsuario,"piernas",str(usuario.piernas),n)
    guardadoCarpeta(nombreUsuario,"botas",str(usuario.pies),n)
    guardadoCarpeta(nombreUsuario,"escudo",str(usuario.escudo),n)
    guardadoCarpeta(nombreUsuario,"critico",str(usuario.critico),n)
    guardadoCarpeta(nombreUsuario,"clase",str(usuario.clase),n)
    guardadoCarpeta(nombreUsuario,"Diamantes",str(usuario.diamantes),n)
    guardadoCarpeta(nombreUsuario,"Amatistas",str(usuario.amatistas),n)
    n="2"

def guardar(n: str) -> None:
    
    reg(usuario.nombre,n)
    barrita('GUARDANDO')
    os.system("cls")



def main() -> None:
    while True:

        while True:
            restaurar()
            estadoJugador()
            os.system("echo.")
            print("para combatir presione \"w\"")
            print("para ir a la tienda presione \"T\"")
            print("para ir a la mochila presione \"M\"")
            print("para guardar sesion presione \"G\"")
            print("para cerrar sesion presione \"C\"")
            print("\n\n\n\n\n\n\nNO OLVIDES GUARDAR TU SESION DE USUARIO, PARA NO PERDER TU PROGRESO \n\n\n\n\n\n\n")
            parametro=input("ingrese una accion:")

            if parametro=="w" or parametro=="W":
                os.system("cls")
                combate()
            elif parametro=="t" or parametro=="T":
                os.system("cls")
                tienda()
            elif parametro=="m" or parametro=="M":
                os.system("cls")
                Mochila()
            elif parametro=="g" or parametro=="G":
                os.system("cls")
                guardar(m)
            elif parametro=="C" or parametro=="c":
                os.system("cls")
                login()
            else:
                charlantina()
                break
    
if __name__=='__main__':
    main()
