import os
import abc

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

    def ataque(self) -> int:
        return 0










class mobs(metaclass=abc.ABCMeta):
    
    def __init__(
        self,
        vidaMaxima:int,
        ARMA: 'arma',
        nombre:str
    ) -> None:

        self.vidaMaxima=vidaMaxima
        self.ARMA=ARMA
        self.nombre=nombre
        self.vidaActual=vidaMaxima
     
    @abc.abstractmethod
    def armaAtaque(self)->int:
        pass
    
    @abc.abstractmethod
    def recibiDano(self,monstruo: 'mobs')->None:
        pass

    @abc.abstractmethod
    def atacar(self,monstruoQueRecibe:'mobs')->None:
        pass


class Jugador(mobs):

    monedas=200

    def __init__(self, vidaMaxima: int, ARMA: 'arma', nombre: str) -> None:
        super().__init__(vidaMaxima, ARMA, nombre)
        self.nombre=nombre
        self.vidaMaxima=vidaMaxima

    def armaAtaque(self) -> int:
        armajugador=hacha()
        valor=armajugador.ataque()
        return valor
    
    def recibiDano(self, monstruo: 'mobs') -> None:
        self.vidaActual-=monstruo.armaAtaque()
        if self.vidaActual < 0:
            self.vidaActual=0

    def atacar(self, monstruoQueRecibe: 'mobs') -> None:
        monstruoQueRecibe.recibiDano(self)



class goblin(mobs):

    def __init__(self, vidaMaxima: int, ARMA: 'arma', nombre: str) -> None:
       super().__init__(15, espada, "Goblin")

    def armaAtaque(self) -> int:
        espadaGoblin=espada()
        valor=espadaGoblin.ataque()
        return valor
    
    def recibiDano(self, monstruo: 'mobs') -> None:
        self.vidaActual-=monstruo.armaAtaque()
        if self.vidaActual < 0:
            self.vidaActual=0

    def atacar(self, monstruoQueRecibe: 'mobs') -> None:
        monstruoQueRecibe.recibiDano(self)



class squeleton(mobs):

    def __init__(self, vidaMaxima: int, ARMA: 'arma', nombre: str) -> None:
       super().__init__(18, arco, "Esqueleton")

    def armaAtaque(self) -> int:
        arcosqueleton=arco()
        valor=arcosqueleton.ataque()
        return valor
    
    def recibiDano(self, monstruo: 'mobs') -> None:
        self.vidaActual-=monstruo.armaAtaque()
        if self.vidaActual < 0:
            self.vidaActual=0

    def atacar(self, monstruoQueRecibe: 'mobs') -> None:
        monstruoQueRecibe.recibiDano(self)
