import random
import pandas as pd
bodovi = 0

def main():
    start = Prikaz()
    igrac = Igrac()
    tabla = Polje()
    potez = Igra()
    start.Pocetak()
    igrac.UnosIgraca()
    tabla.provjeri(tabla.getm())
    potez.ispis()
    while True:
        potez.odabir()
        tabla.provjeri(tabla.getm())
        tabla.eliminirajPostaviBoduj(tabla.getm(), bodovi)
        potez.ispis()
        tabla.bodovanje(bodovi)
    potez.kraj()

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

    def getm(self):
        return self.__postavi

    global dell
    dell='dell'

    def provjeri(self, __postavi):
        for x in range(len(list(lista))):
            for y in range(1, len(list(lista)), 1):
                if ((__postavi[0])[x][y-1]==(__postavi[0])[x][y]):
                    __postavi[x][y]+=(dell,)
                    __postavi[x][y + 1]+=(dell,)
                    if ((__postavi[0])[x][y] == (__postavi[0])[x][y + 1]):
                        __postavi[x][y+1]+=(dell,)
                        if ((__postavi[0])[x][y+1]==(__postavi[0])[x][y+2]):
                            __postavi[x][y + 2]+=(dell,)
                        if ((__postavi[0])[x][y + 1] == (__postavi[0])[x-1][y + 1]):
                            __postavi[x-1][y + 1]+=(dell,)
                        if ((__postavi[0])[x][y + 1] == (__postavi[0])[x+1][y + 1]):
                            __postavi[x+1][y + 1]+=(dell,)
                    if((__postavi[0])[x][y] == (__postavi[0])[x - 1][y]):
                        __postavi[x-1][y]+=(dell,)
                        if ((__postavi[0])[x-1][y]==(__postavi[0])[x-2][y]):
                            __postavi[x][y - 2]+=(dell,)
                        if ((__postavi[0])[x-1][y] == (__postavi[0])[x-1][y - 1]):
                            __postavi[x-1][y - 1]+=(dell,)
                        if ((__postavi[0])[x-1][y] == (__postavi[0])[x+1][y + 1]):
                            __postavi[x-1][y + 1]+=(dell,)
                    if((__postavi[0])[x][y] == (__postavi[0])[x + 1][y]):
                        __postavi[x+1][y]+=(dell,)
                        if ((__postavi[0])[x+1][y]==(__postavi[0])[x+2][y]):
                            __postavi[x+2][y]+=(dell,)
                        if ((__postavi[0])[x+1][y] == (__postavi[0])[x+1][y + 1]):
                            __postavi[x+1][y + 1]+=(dell,)
                        if ((__postavi[0])[x+1][y] == (__postavi[0])[x+1][y - 1]):
                            __postavi[x+1][y - 1]+=(dell,)
                    if((__postavi[0])[x][y - 1] == (__postavi[0])[x - 1][y-1]):
                        __postavi[x-1][y-1]+=(dell,)
                        if ((__postavi[0])[x-1][y-1]==(__postavi[0])[x-1][y-2]):
                            __postavi[x-1][y - 2]+=(dell,)
                        if ((__postavi[0])[x-1][y - 1] == (__postavi[0])[x-1][y]):
                            __postavi[x-1][y]+=(dell,)
                        if ((__postavi[0])[x-1][y - 1] == (__postavi[0])[-2][y - 1]):
                            __postavi[x-2][y - 1]+=(dell,)
                    if((__postavi[0])[x][y - 1] == (__postavi[0])[x + 1][y-1 ]):
                        __postavi[x+1][y-1]+=(dell,)
                        if ((__postavi[0])[x+1][y-1]==(__postavi[0])[x+2][y-1]):
                            __postavi[x+2][y - 2]+=(dell,)
                        if ((__postavi[0])[x+1][y - 1] == (__postavi[0])[x+1][y - 2]):
                            __postavi[x-1][y -2]+=(dell,)
                        if ((__postavi[0])[x+1][y - 1] == (__postavi[0])[x+1][y]):
                            __postavi[x+1][y]+=(dell,)

    def eliminirajPostaviBoduj(self, __postavi, bodovi):
        for x in range(10):
            for y in range(10):
                if ('dell' in __postavi[x][y]):
                    if 'obicni' in __postavi[x][y]:
                        bodovi+=10
                        __postavi[x][y].pop()
                        __postavi[x][y]+=[(random.choice(Extras.slatkisi()),\
                                           random.choice(Extras.vrste()))]
                    if ('nagradni' in __postavi[x][y]):
                        bodovi+=50
                        __postavi[x][y].pop()
                        __postavi[x][y] += [(random.choice(Extras.slatkisi()),\
                                             random.choice(Extras.vrste()))]
                    if (('nagradni', 'bomba') in __postavi[x][y]):
                        for i in __postavi[x]:
                            if 'obicni' in i:
                                bodovi += 10
                            if 'nagradni' in i:
                                bodovi += 50
                        __postavi[x].pop(0)
                        __postavi[x][y] += [(random.choice(Extras.slatkisi()),\
                                             random.choice(Extras.vrste())) \
                                             for z in range(10)]

    def bodovanje(self, bodovi):
        print(f"Trenutni broj bodova je: {bodovi}")
        return bodovi

class Igra(Polje, Igrac):
    def odabir(self):
        nesto=super().getm()
        temp=None
        print('Unesi broj redka i stupca elemenata kojima bi zamijenio pozicije...')
        zamjena1_red=int(input('\n'+'Red u kojem je element za zamjenu: '))
        zamjena1_stupac =int( input('\n' + 'Stupac u kojem je element za zamjenu: '))
        zamjena2_red =int( input('\n' + 'Redak elementa s kojim bi ga zamijenio/la: '))
        zamjena2_stupac =int( input('\n' + 'Stupac elementa s kojim bi ga zamijenio/la: '))
        if ((zamjena1_red==(zamjena2_red-1) or zamjena1_red==(zamjena2_red+1) or zamjena1_red==(zamjena2_red))\
            and (zamjena1_stupac==(zamjena2_stupac-1) or zamjena1_stupac==(zamjena2_stupac+1) or zamjena1_stupac==(zamjena2_stupac))):
            temp=nesto[zamjena1_red][zamjena1_stupac]
            nesto[zamjena1_red][zamjena1_stupac]=nesto[zamjena2_red][zamjena2_stupac]
            nesto[zamjena2_red][zamjena2_stupac]=temp
        else:
            print('Morate odabrati susjedne elemente!')

    def ispis(self):
        nesto=super().getm()
        df1 = pd.DataFrame(nesto, columns=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        df1.sort_values(by=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        pd.options.display.max_rows = 1000
        pd.options.display.min_rows = 10
        pd.options.display.max_columns = 1000
        pd.options.display.min_rows = 10
        pd.options.display.width = 1000
        pd.set_option("expand_frame_repr", True)
        print(df1)

    def kraj(self):
        idd=super().getIgrac()
        bod=super().bodovanje()
        print(f'Igrač {idd} je osvojio {bod} bodova. Cestitam!')

        return

main()
