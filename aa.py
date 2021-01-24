import random

def main(object):
    while True:
        Elementi=Extras()
        start=Prikaz()
        start.Pocetak()
        igrac=Igrac()
        igrac.UnosIgraca()
        tabla=Polje()
        tabla.provjeri()
        potez=Igra()
        potez.odabir()
        tabla.eliminirajPostaviBoduj()
        tabla.provjeri()

class Extras(object):
    __slatkis=['crni', 'crveni', 'plavi', 'zeleni', 'zuti', 'ljubicasti']

    __vrsta=['nagradni']*30+['obicni']*100+['bombe']*10
    random.shuffle(__vrsta)

    @staticmethod
    def slatkisi():
        return Extras.__slatkis[:]

    @staticmethod
    def vrste():
        return Extras.__vrsta[:]

    def __init__(self, slatkis, vrsta):
        self.__slatkis=slatkis
        self.__vrsta=vrsta

    @property
    def slatkis(self):
        return self.__slatkis

    @property
    def vrsta(self):
        return self.__vrsta

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r)' % (self.vrsta, self.slatkis)

    def __str__(self):
        return self.slatkis.title() + ' ' + self.vrsta

class Prikaz(object):
    def Pocetak(self):
        print('Dobrodošli u igru Match-3-puzzle'+'_'*40+'\n')

class Igrac(object):
    def UnosIgraca(self):
        while True:
            ID=input('Unesi naziv igraca: ')
            if ID.strip():
                print('\n'+'_'*50+'\n')
                return ID

class Igra(object):
    def odabir(self):
        zamjena=input('\n'+'Unesi broj redka pa stupca od elementa koji bi zamijenio: ')
        zaZamijeniti=input('\n'+'Unesi broj redka pa stupca od elementa s kojim bi ga zamijenio: ')

class Polje(object):
    def __init__(self):
        self.__postavi=[[(random.choice(Extras.slatkisi()), random.choice(Extras.vrste())) for x in range(10)] for z in range(10)]

    bodovi = 0

    def provjeri(self, __postavi):
        for x in range(10):
            for y in range(10):
                if (__postavi[x][y-1]==__postavi[x][y]):
                    __postavi[x][y].append('dell')
                    __postavi[x][y + 1].append('dell')
                    if (__postavi[x][y] == __postavi[x][y + 1]):
                        __postavi[x][y+1].append('dell')
                        if (__postavi[x][y+1]==__postavi[x][y+2]):
                            __postavi[x][y + 2].append('dell')
                        if (__postavi[x][y + 1] == __postavi[x-1][y + 1]):
                            __postavi[x-1][y + 1].append('dell')
                        if (__postavi[x][y + 1] == __postavi[x+1][y + 1]):
                            __postavi[x+1][y + 1].append('dell')
                    if(__postavi[x][y] == __postavi[x - 1][y]):
                        __postavi[x-1][y].append('dell')
                        if (__postavi[x-1][y]==__postavi[x-2][y]):
                            __postavi[x][y - 2].append('dell')
                        if (__postavi[x-1][y] == __postavi[x-1][y - 1]):
                            __postavi[x-1][y - 1].append('dell')
                        if (__postavi[x-1][y] == __postavi[x+1][y + 1]):
                            __postavi[x-1][y + 1].append('dell')
                    if(__postavi[x][y] == __postavi[x + 1][y]):
                        __postavi[x+1][y].append('dell')
                        if (__postavi[x+1][y]==__postavi[x+2][y]):
                            __postavi[x+2][y].append('dell')
                        if (__postavi[x+1][y] == __postavi[x+1][y + 1]):
                            __postavi[x+1][y + 1].append('dell')
                        if (__postavi[x+1][y] == __postavi[x+1][y - 1]):
                            __postavi[x+1][y - 1].append('dell')
                    if(__postavi[x][y - 1] == __postavi[x - 1][y-1]):
                        __postavi[x-1][y-1].append('dell')
                        if (__postavi[x-1][y-1]==__postavi[x-1][y-2]):
                            __postavi[x-1][y - 2].append('dell')
                        if (__postavi[x-1][y - 1] == __postavi[x-1][y]):
                            __postavi[x-1][y].append('dell')
                        if (__postavi[x-1][y - 1] == __postavi[-2][y - 1]):
                            __postavi[x-2][y - 1].append('dell')
                    if(__postavi[x][y - 1] == __postavi[x + 1][y-1 ]):
                        __postavi[x+1][y-1].append('dell')
                        if (__postavi[x+1][y-1]==__postavi[x+2][y-1]):
                            __postavi[x+2][y - 2].append('dell')
                        if (__postavi[x+1][y - 1] == __postavi[x+1][y - 2]):
                            __postavi[x-1][y -2].append('dell')
                        if (__postavi[x+1][y - 1] == __postavi[x+1][y]):
                            __postavi[x+1][y].append('dell')
        return

    def eliminirajPostaviBoduj(self, __postavi, bodovi):
        for x in range(10):
            for y in range(10):
                if 'dell' in __postavi[x][y]:
                    if 'obicni' in __postavi[x][y]:
                        bodovi+=10
                        __postavi[x][y].pop()
                    if 'nagradni' in __postavi[x][y]:
                        bodovi+=50
                        __postavi[x][y].pop()
                    if ('nagradni', 'bomba') in __postavi[x][y]:
                        for i in __postavi[x]:
                            if 'obicni' in i:
                                bodovi += 10
                            if 'nagradni' in i:
                                bodovi += 50
                        __postavi[x].pop(0)
                        [(random.choice(Extras.slatkisi()),\
                          random.choice(Extras.vrste()))\
                         for x in range(10)]
                else:
                    return False
        
