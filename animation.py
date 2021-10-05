import os
import keyboard as kb
import random

parametroizq=0
parametrodrc=6
parametroarr=0
parametroabj=6
Bparametroizq=0
Bparametrodrc=1
Bparametroarr=0
Bparametroabj=1
Bparametroizq1=0
Bparametrodrc1=9
Bparametroarr1=0
Bparametroabj1=9


lista=[]
lista2=[]

jugador="pp"
mob="bb"
mob1="gg"


def pulsaciones() -> None:

    tecla=kb.read_key()

    if tecla=="flecha izquierda":
        os.system("cls")
        lista2.append(1)
    elif tecla=="flecha derecha":
        os.system("cls")
        lista2.append(2)
    elif tecla=="flecha arriba":
        os.system("cls")
        lista2.append(3)
    elif tecla=="flecha abajo":
        os.system("cls")
        lista2.append(4)

def mobs1(parm1,parm2,parm3,parm4,Bparm1,Bparm2,Bparm3,Bparm4,mob):
    
    moduloJugado1=(parm2-parm1)-(Bparm2-Bparm1)
    moduloJugado2=(parm4-parm3)-(Bparm4-Bparm3)
    if (moduloJugado1>=1 or moduloJugado1 <=(-1)) or (moduloJugado2>=2 or moduloJugado2 <=(-1)):
        lista[Bparm4-Bparm3-1][Bparm2-Bparm1-1]=mob
        if Bparm2-Bparm1-1 < 11 and lista[Bparm4-Bparm3-1][11]!=jugador:
            lista[Bparm4-Bparm3-1][11]=" "
        if Bparm4-Bparm3==parm4-parm3 or Bparm4-Bparm3==parm4-parm3-1:
            for i in range(len(lista)):
                if i!=Bparm4-Bparm3-1:
                    if Bparm4-Bparm3==parm4-parm3:
                        lista[parm4-parm3-1][parm2-parm1-2]=""
                        if parm4-parm3==Bparm4-Bparm3 and parm2-parm1-1==Bparm2-Bparm1:
                            lista[parm4-parm3-1][parm2-parm1-2]=mob
                            lista[parm4-parm3-1][parm2-parm1-3]=""
                    if parm4-parm3==Bparm4-Bparm3 and parm2-parm1<Bparm2-Bparm1:
                            lista[parm4-parm3-1][parm2-parm1-2]=" "
                            for i in range(len(lista)):
                                if i!=Bparm4-Bparm3-1:
                                    lista[i][11]="   "
                                if Bparm4-Bparm3==parm4-parm3:
                                    lista[parm4-parm3-2][11]="  "
                                if Bparm4-Bparm3==parm4-parm3-1:
                                    lista[parm4-parm3-1][11]="  "
                    if Bparm4-Bparm3==parm4-parm3-1:
                        lista[parm4-parm3-2][parm2-parm1-2]=""
                        if parm4-parm3-1==Bparm4-Bparm3 and parm2-parm1-1==Bparm2-Bparm1:
                            lista[parm4-parm3-2][parm2-parm1-2]=mob
                            lista[parm4-parm3-2][parm2-parm1-3]=""
                        if parm4-parm3-1==Bparm4-Bparm3 and parm2-parm1<Bparm2-Bparm1:
                            lista[parm4-parm3-2][parm2-parm1-2]=" "
                            for i in range(len(lista)):
                                if i!=Bparm4-Bparm3-1:
                                    lista[i][11]="   "
                                if Bparm4-Bparm3==parm4-parm3:
                                    lista[parm4-parm3-2][11]="  "
                                if Bparm4-Bparm3==parm4-parm3-1:
                                    lista[parm4-parm3-1][11]="  "
            
    elif moduloJugado1==0 and (moduloJugado2>=0 or moduloJugado2<=1):
        lo=Bparm2
        Bparm2=lo+1
        lista[Bparm4-Bparm3-1][Bparm2-Bparm1-1]=mob
        for i in range(len(lista)):
            if i!=Bparm4-Bparm3-1:
                lista[i][11]="   "
                if Bparm4-Bparm3==parm4-parm3:
                    lista[parm4-parm3-2][11]="  "
                if Bparm4-Bparm3==parm4-parm3-1:
                    lista[parm4-parm3-1][11]="  "

    if (moduloJugado1>=-2 and moduloJugado1<=2) and (moduloJugado2>=-2 and moduloJugado2<=3):
        print("habilitado"+mob)


def interacciones(parm1,parm2,parm3,parm4,Bparm1,Bparm2,Bparm3,Bparm4,Bparm11,Bparm21,Bparm31,Bparm41,mob,mob1):
    if ((parm4-parm3==Bparm41-Bparm31 or parm4-parm3-1==Bparm41-Bparm31) and lista[Bparm4-Bparm3-1][11]!=mob) and Bparm21-Bparm11>parm2-parm1:
        lista[Bparm4-Bparm3-1][11]="  "
    elif ((parm4-parm3==Bparm41-Bparm31 or parm4-parm3-1==Bparm41-Bparm31) and lista[Bparm4-Bparm3-1][11]!=mob) and Bparm21-Bparm11<parm2-parm1:
        lista[Bparm4-Bparm3-1][11]=" "

    if (parm4-parm3==Bparm4-Bparm3 or parm4-parm3-1==Bparm4-Bparm3) and Bparm2-Bparm1>parm2-parm1:
        if lista[Bparm41-Bparm31-1][11]!=mob1:
            lista[Bparm41-Bparm31-1][11]="  "
        elif lista[Bparm41-Bparm31-1][11]==mob1:
            lista[Bparm41-Bparm31-1][11]=(mob1+" ")


def animacion(parm1: int,parm2: int,parm3: int,parm4: int) -> None:
    for i in range(12):
        lista.append([])
        global glob1
        global glob2
        global glob3
        global glob4

        if (i+1)>=(parm4-parm3)-1 and (i+1)<=(parm4-parm3):
            for f in range(12):
                if (f+1)==(parm2-parm1):    
                    lista[i].append(jugador)
                elif (parm2-parm1)>12 and (f+1)==12:
                    lista[i].append(jugador)
                    glob1=12
                    glob2=0
                elif (parm2-parm1)<1 and (f+1)==1:
                    lista[i].append(jugador)
                    glob1=1
                    glob2=0
                else:
                    lista[i].append(" ")
        elif (parm4-parm3)>12 and ((i+1)==12 or (i+2)==12):
            for f in range(12):
                if (f+1)==(parm2-parm1):    
                    lista[i].append(jugador)
                elif (parm2-parm1)>12 and (f+1)==12:
                    lista[i].append(jugador)
                    glob1=12
                    glob2=0
                elif (parm2-parm1)<1 and (f+1)==1:
                    lista[i].append(jugador)
                    glob1=1
                    glob2=0
                else:
                    lista[i].append(" ")
                glob4=12
                glob3=0
        elif (parm4-parm3)<2 and ((i+1)==2 or (i+2)==2):
            for f in range(12):
                if (f+1)==(parm2-parm1):    
                    lista[i].append(jugador)
                elif (parm2-parm1)>12 and (f+1)==12:
                    lista[i].append(jugador)
                    glob1=10
                    glob2=0
                elif (parm2-parm1)<1 and (f+1)==1:
                    lista[i].append(jugador)
                    glob1=1
                    glob2=0
                else:
                    lista[i].append(" ")
                glob4=2
                glob3=0

        else:
            for f in range(11):
                lista[i].append(" ")
            for f in range(1):
                lista[i].append("  ")
    


def main1(parametroizq,parametrodrc,parametroarr,parametroabj,Bparametroizq,Bparametrodrc,Bparametroarr,Bparametroabj,Bparametroizq1,Bparametrodrc1,Bparametroarr1,Bparametroabj1,mob,mob1,lista,lista2):
    
    while True:

        os.system("cls")
        print("\n\n\n\n")

        animacion(parametroizq,parametrodrc,parametroarr,parametroabj)

        ran=random.randint(0,100)
        ran1=random.randint(0,100)

        if ran >=0 and ran <=23:
            Bparametroizq+=1
        elif ran >=24 and ran <=50:
            Bparametrodrc+=1
        elif ran >=51 and ran <=73:
            Bparametroarr+=1
        elif ran >=74 and ran <=100:
            Bparametroabj+=1

        if ran1 >=0 and ran1 <=23:
            Bparametroizq1+=1
        elif ran1 >=24 and ran1 <=50:
            Bparametrodrc1+=1
        elif ran1 >=51 and ran1 <=73:
            Bparametroarr1+=1
        elif ran1 >=74 and ran1 <=100:
            Bparametroabj1+=1

        if Bparametrodrc-Bparametroizq<1:
            Bparametroizq=0
            Bparametrodrc=1
        elif Bparametrodrc-Bparametroizq>12:
            Bparametroizq=0
            Bparametrodrc=12
        if Bparametroabj-Bparametroarr<1:
            Bparametroarr=0
            Bparametroabj=1
        elif Bparametroabj-Bparametroarr>12:
            Bparametroarr=0
            Bparametroabj=12
        if Bparametrodrc1-Bparametroizq1<1:
            Bparametroizq1=0
            Bparametrodrc1=1
        elif Bparametrodrc1-Bparametroizq1>12:
            Bparametroizq1=0
            Bparametrodrc1=12
        if Bparametroabj1-Bparametroarr1<1:
            Bparametroarr1=0
            Bparametroabj1=1
        elif Bparametroabj1-Bparametroarr1>12:
            Bparametroarr1=0
            Bparametroabj1=12
            
        
        
        mobs1(parametroizq,parametrodrc,parametroarr,parametroabj,Bparametroizq,Bparametrodrc,Bparametroarr,Bparametroabj,mob)
        mobs1(parametroizq,parametrodrc,parametroarr,parametroabj,Bparametroizq1,Bparametrodrc1,Bparametroarr1,Bparametroabj1,mob1)
        interacciones(parametroizq,parametrodrc,parametroarr,parametroabj,Bparametroizq,Bparametrodrc,Bparametroarr,Bparametroabj,Bparametroizq1,Bparametrodrc1,Bparametroarr1,Bparametroabj1,mob,mob1)

        for i in range(len(lista)):
            print(f"                                          {lista[i]}")

        lista.clear()

        if parametrodrc-parametroizq > 12 or parametrodrc-parametroizq < 1:

            if glob1==12:
                parametroizq=glob2
                parametrodrc=glob1
            elif glob1==1:
                parametroizq=glob2
                parametrodrc=glob1

        if parametroabj-parametroarr > 12 or parametroabj-parametroarr < 2:

            if glob4==12:
                parametroabj=glob4
                parametroarr=glob3
            elif glob4==2:
                parametroabj=glob4
                parametroarr=glob3

        pulsaciones()
        
        if lista2[0]==1:
            parametroizq+=1
            lista2.clear()
        elif lista2[0]==2:
            parametrodrc+=1
            lista2.clear()
        elif lista2[0]==3:
            parametroarr+=1
            lista2.clear()
        elif lista2[0]==4:
            parametroabj+=1
            lista2.clear()

if __name__=='__main__':
    main1(parametroizq,parametrodrc,parametroarr,parametroabj,Bparametroizq,Bparametrodrc,Bparametroarr,Bparametroabj,Bparametroizq1,Bparametrodrc1,Bparametroarr1,Bparametroabj1,mob,mob1,lista,lista2)
