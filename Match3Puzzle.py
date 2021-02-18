import random

bodovi = 0

def main():
    start = Prikaz()
    igrac = Igrac()
    tabla = Polje()
    potez = Igra()
    start.Pocetak()
    igrac.UnosIgraca()
    while True:
        tabla.provjeri(tabla.getm())
        tabla.ispis()
        potez.odabir()
        tabla.eliminirajPostaviBoduj(tabla.getm(), bodovi)

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

class Slatkisi(object):

    def __init__(self):
        self.__extrasi = []
        for vrsta in Extras.__vrsta():
            for slatkis in Extras.__slatkis():
                self.__extrasi.append(Extras(vrsta=vrsta, slatkis=slatkis))

    def __str__(self, red=4, sirina=15):
        ispis = ""
        i = 0
        for extras in self.__extrasi:
            ispis += str(extras).ljust(sirina, ' ')
            i += 1
            if i == red:
                ispis += '\n'
                i = 0
        return ispis

    def mjesanje_slatkisa():
        for i in range(40):
            random.shuffle(self.__extrasi)


class Prikaz(object):
    def Pocetak(self):
        print('Dobrodošli u igru Match-3-puzzle'+'_'*40+'\n')

class Igrac(object):
    def UnosIgraca(self):
            ID=input('Unesi naziv igraca: ')
            if ID.strip():
                print('\n'+'_'*50+'\n')

    @staticmethod
    def getIgrac(self):
        return ID

class Polje(object):
    def __init__(self):
        self.__postavi=[[(random.choice(Extras.slatkisi()), random.choice(Extras.vrste())) for x in range(10)] for z in range(10)]

        global lista
        lista = iter(self.__postavi)

    def ispis(self):
        for i in range(10):
            for j in range(10):
                print(self.__postavi[i][j], end=" ")
            print()

    def getm(self):
        return self.__postavi

    global dell
    dell='dell'

    def provjeri(self, __postavi):
        for x in range(len(list(lista))):
            for y in range(len(list(lista))):
                if (__postavi[x][y-1]==__postavi[x][y]):
                    __postavi[x][y]+=(dell,)
                    __postavi[x][y + 1]+=(dell,)
                    if (__postavi[x][y] == __postavi[x][y + 1]):
                        __postavi[x][y+1]+=(dell,)
                        if (__postavi[x][y+1]==__postavi[x][y+2]):
                            __postavi[x][y + 2]+=(dell,)
                        if (__postavi[x][y + 1] == __postavi[x-1][y + 1]):
                            __postavi[x-1][y + 1]+=(dell,)
                        if (__postavi[x][y + 1] == __postavi[x+1][y + 1]):
                            __postavi[x+1][y + 1]+=(dell,)
                    if(__postavi[x][y] == __postavi[x - 1][y]):
                        __postavi[x-1][y]+=(dell,)
                        if (__postavi[x-1][y]==__postavi[x-2][y]):
                            __postavi[x][y - 2]+=(dell,)
                        if (__postavi[x-1][y] == __postavi[x-1][y - 1]):
                            __postavi[x-1][y - 1]+=(dell,)
                        if (__postavi[x-1][y] == __postavi[x+1][y + 1]):
                            __postavi[x-1][y + 1]+=(dell,)
                    if(__postavi[x][y] == __postavi[x + 1][y]):
                        __postavi[x+1][y]+=(dell,)
                        if (__postavi[x+1][y]==__postavi[x+2][y]):
                            __postavi[x+2][y]+=(dell,)
                        if (__postavi[x+1][y] == __postavi[x+1][y + 1]):
                            __postavi[x+1][y + 1]+=(dell,)
                        if (__postavi[x+1][y] == __postavi[x+1][y - 1]):
                            __postavi[x+1][y - 1]+=(dell,)
                    if(__postavi[x][y - 1] == __postavi[x - 1][y-1]):
                        __postavi[x-1][y-1]+=(dell,)
                        if (__postavi[x-1][y-1]==__postavi[x-1][y-2]):
                            __postavi[x-1][y - 2]+=(dell,)
                        if (__postavi[x-1][y - 1] == __postavi[x-1][y]):
                            __postavi[x-1][y]+=(dell,)
                        if (__postavi[x-1][y - 1] == __postavi[-2][y - 1]):
                            __postavi[x-2][y - 1]+=(dell,)
                    if(__postavi[x][y - 1] == __postavi[x + 1][y-1 ]):
                        __postavi[x+1][y-1]+=(dell,)
                        if (__postavi[x+1][y-1]==__postavi[x+2][y-1]):
                            __postavi[x+2][y - 2]+=(dell,)
                        if (__postavi[x+1][y - 1] == __postavi[x+1][y - 2]):
                            __postavi[x-1][y -2]+=(dell,)
                        if (__postavi[x+1][y - 1] == __postavi[x+1][y]):
                            __postavi[x+1][y]+=(dell,)

    def eliminirajPostaviBoduj(self, __postavi, bodovi):
        for x in range(10):
            for y in range(10):
                if 'dell' in __postavi[x][y]:
                    if 'obicni' in __postavi[x][y]:
                        bodovi+=10
                        __postavi[x][y].pop()
                        __postavi[x][y]+=[(random.choice(Extras.slatkisi()),\
                                           random.choice(Extras.vrste()))]
                    if 'nagradni' in __postavi[x][y]:
                        bodovi+=50
                        __postavi[x][y].pop()
                        __postavi[x][y] += [(random.choice(Extras.slatkisi()),\
                                             random.choice(Extras.vrste()))]
                    if ('nagradni', 'bomba') in __postavi[x][y]:
                        for i in __postavi[x]:
                            if 'obicni' in i:
                                bodovi += 10
                            if 'nagradni' in i:
                                bodovi += 50
                        __postavi[x].pop(0)
                        __postavi[x][y] += [(random.choice(Extras.slatkisi()),\
                                             random.choice(Extras.vrste())) \
                                             for z in range(10)]



    @staticmethod
    def bodovanje(self):
        return bodovi

class Igra(Polje):
    def odabir(self):
        nesto=super().getm()
        bolic=1
        while bolic:
            print('Unesi broj redka i stupca elemenata kojima bi zamijenio pozicije...')
            zamjena1_red=int(input('\n'+'Red u kojem je element za zamjenu: '))
            zamjena1_stupac =int( input('\n' + 'Stupac u kojem je element za zamjenu: '))
            zamjena2_red =int( input('\n' + 'Redak elementa s kojim bi ga zamijenio/la: '))
            zamjena2_stupac =int( input('\n' + 'Stupac elementa s kojim bi ga zamijenio/la: '))
            if ((zamjena1_red==(zamjena2_red-1) or zamjena1_red==(zamjena2_red+1) or zamjena1_red==(zamjena2_red))\
                and (zamjena1_stupac==(zamjena2_stupac-1) or zamjena1_stupac==(zamjena2_stupac+1) or zamjena1_stupac==(zamjena2_stupac))):
                nesto[zamjena1_red][zamjena1_stupac], \
                nesto[zamjena2_red][zamjena2_stupac] = \
                nesto[zamjena2_red][zamjena2_stupac], \
                nesto[zamjena1_red][zamjena1_stupac]
            else:
                print('Morate odabrati susjedne elemente!')
                break

        return zamjena1_red, zamjena2_red, zamjena1_stupac, zamjena2_stupac

main()
