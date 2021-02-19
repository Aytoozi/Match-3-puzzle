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

class Prikaz(object):
    def Pocetak(self):
        print('Dobrodošli u igru Match-3-puzzle'+'_'*40+'\n')

class Igrac(object):
    def UnosIgraca(self):
            ID=input('Unesi naziv igraca: ')
            if ID.strip():
                print('\n'+'_'*50+'\n')

    def getIgrac(self, ID):
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
        prethodni = sljedeci = None
        l = len(__postavi)
        for index, obj in enumerate(__postavi):
            if index > 0:
                prethodni = __postavi[index - 1]
            if index < (l - 1):
                sljedeci = __postavi[index + 1]
        for x in range(len(list(lista))-2):
            for y in range(1, len(list(lista))-2, 1):
                if ((__postavi[0])[x][y-1]==(__postavi[0])[x][y]):
                    __postavi[x][y]+=(dell,)
                    __postavi[x][y-1]+=(dell,)
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
                else:
                    pass

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
        return bodovi

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
        bod=super().bodovanje(bodovi)
        print(f'Igrač {idd} ima {bod} bodova. Bravo!')
        return

main()
