import os
import abc


class armadura(metaclass=abc.ABCMeta):
    nombreArmadura=""
    
    @abc.abstractmethod
    def defensa(self) -> int:
        pass


class cascoCuero(armadura):

    nombreArmadura="Casco de Cuero"

    def defensa(self) -> int:
        return 1

class chalecoCuero(armadura):

    nombreArmadura="Chaleco de Cuero"

    def defensa(self) -> int:
        return 2

class piernasCuero(armadura):

    nombreArmadura="Pantalon de Cuero"

    def defensa(self) -> int:
        return 1

class botasCuero(armadura):

    nombreArmadura="Botas de Cuero"
    
    def defensa(self) -> int:
        return 1

class escudoHierro(armadura):

    nombreArmadura="Escudo de Hierro"

    def defensa(self) -> int:
        return 2

class vacia(armadura):

    nombreArmadura="Vacio"

    def defensa(self) -> int:
        return 0
        




class arma(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def ataque(self) -> int:
        pass


class espada(arma):

    nombreArma="ESPADA"
    inflingedano="espada ---> 5"

    def ataque(self) -> int:
        return 5


class arco(arma):

    nombreArma="ARCO"
    inflingedano="arco ---> 6"

    def ataque(self) -> int:
        return 6

class hacha(arma):

    nombreArma="HACHA"
    inflingedano="HACHA ---> 7"

    def ataque(self) -> int:
        return 7

class cetroMagico(arma):
    
    nombreArma="CETRO"
    inflingedano="CETRO ---> 7"

    def ataque(self) -> int:
        return 7

class espadaHierro(arma):
    
    nombreArma="ESPADA DE HIERRO"
    inflingedano="ESPADA DE HIERRO ---> 7"

    def ataque(self) -> int:
        return 7 

class arcoPlatinado(arma):
    
    nombreArma="ARCO PLATINADO"
    inflingedano="ARCO PLATINADO ---> 7"

    def ataque(self) -> int:
        return 7               

class katana(arma):

    nombreArma="KATANA"
    inflingedano="katana ---> 9"

    def ataque(self) -> int:
        return 9


class martillo(arma):

    nombreArma="MARTILLO"
    inflingedano="espada ---> 11"

    def ataque(self) -> int:
        return 11



class samrtSword(arma):

    nombreArma="ESPADA INTELIGENTE"
    inflingedano="espada inteligente ---> 15"

    def ataque(self) -> int:
        return 15

class vacio(arma):
    nombreArma="NINGUNA"
    inflingedano="NADA ---> 0"

    def ataque(self) -> int:
        return 0





class mobs(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __init__(
        self,
        vidaMaxima:int,
        ARMA: 'arma',
        nombre:str,
        casco: 'armadura',
        pecho: 'armadura',
        piernas: 'armadura',
        pies: 'armadura',
        escudo: 'armadura'
    ) -> None:

        self.vidaMaxima=vidaMaxima
        self.ARMA=ARMA
        self.nombre=nombre
        self.vidaActual=vidaMaxima
        self.casco=casco
        self.pecho=pecho
        self.piernas=piernas
        self.pies=pies
        self.escudo=escudo
        self.ataqueBase=0
        self.defensaBase=0
        self.clase=""

    def armaAtaque(self) -> int:
        armajugador=self.ARMA()
        valor=(armajugador.ataque()+self.ataqueBase)
        return valor
    
    def defensaArmadura(self) -> int:
        cascoJugador=self.casco()
        pechoJugador=self.pecho()
        piernasJugador=self.piernas()
        piesJugador=self.pies()
        escudoJugador=self.escudo()
        valor=cascoJugador.defensa()+pechoJugador.defensa()+piernasJugador.defensa()+piesJugador.defensa()+escudoJugador.defensa()+self.defensaBase
        return valor

    def recibiDano(self, monstruo: 'mobs') -> None:
        muestradaño=(monstruo.armaAtaque()-self.defensaArmadura())
        if muestradaño >= 0:
            self.vidaActual-=muestradaño
            if self.vidaActual < 0:
                self.vidaActual=0
        else:
            self.vidaActual-=0

        
    def atacar(self, monstruoQueRecibe: 'mobs') -> None:
        monstruoQueRecibe.recibiDano(self)


class Jugador(mobs):

    monedas=200
    nivel=1
    experiencia=0
    critico=0


    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

        super().__init__(vidaMaxima, ARMA, nombre, casco, pecho, piernas, pies, escudo)
        self.nombre=nombre
        self.vidaMaxima=vidaMaxima


class goblin(mobs):

    nivel=1
    nombre="GOBLIN"
    monedass=10
    expe=40

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(15, espada, "Goblin", casco, pecho, piernas, pies, escudo)

class goblin5(mobs):
    
    nivel=5
    nombre="GOBLIN"
    monedass=35
    expe=100

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(30, hacha, "Goblin", casco, pecho, piernas, pies, escudo)


class squeleton(mobs):

    nivel=1
    nombre="ESQUELETO"
    monedass=20
    expe=70

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(18, arco, "Esqueleton", casco, pecho, piernas, pies, escudo)

class squeleton5(mobs):
    
    nivel=5
    nombre="ESQUELETO"
    monedass=50
    expe=150

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(50, katana, "Esqueleton", casco, pecho, piernas, pies, escudo)


class scorpion(mobs):
    
    nivel=1
    nombre="Scorpion"
    monedass=20
    expe=70

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(20, hacha, "Escorpion", casco, pecho, piernas, pies, escudo)


class scorpion5(mobs):
    
    nivel=5
    nombre="ESQUELETO"
    monedass=50
    expe=200

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(30, martillo, "Scorpion", casco, pecho, piernas, pies, escudo)

class minotauro(mobs):
    
    nivel=1
    nombre="MINOTAURO"
    monedass=40
    expe=120

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(25, katana, "Minotauro", casco, pecho, piernas, pies, escudo)

class minotauro5(mobs):
    
    nivel=5
    nombre="ESQUELETO"
    monedass=150
    expe=350

    def __init__(
        self,
        vidaMaxima: int, 
        ARMA: 'arma', 
        nombre: str, 
        casco: 'armadura', 
        pecho: 'armadura', 
        piernas: 'armadura', 
        pies: 'armadura', 
        escudo: 'armadura'
        ) -> None:

       super().__init__(75, samrtSword, "Minotauro", casco, pecho, piernas, pies, escudo)   
