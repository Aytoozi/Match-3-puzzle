class Extras(object):
#kljuc je broj, vrijednosti su boja i broj bodova koji taj slatkis nosi
    __slatkis_info={
        1: ('crni', 50),
        2: ('crveni', 100),
        3: ('plavi', 150)
                    }
    __vrsta= ['obicni', 'bombe', 'nagradni']

    @staticmethod
    def brojevi():
        return Extras.__slatkis_info.keys()
    @staticmethod
    def vrste():
        return Extras.__vrsta[:]

    def __init__(self, broj, vrsta):
        self.__broj=int(broj)
        self.__vrsta=vrsta

    @property
    def broj(self):
        return self.__broj

    @property
    def vrsta(self):
        return self.__vrsta

    @property
    def boja(self):
        return Extras.__slatkis_info[self.__broj][0]

    @property
    def bod(self):
        return Extras.__slatkis_info[self.__broj][1]

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r)' % (self.vrsta, self.boja)

    def __str__(self):
        return self.boja.title() + ' ' + self.vrsta

for vrsta in Extras.vrste():
    for broj in Extras.brojevi():
        e=Extras(broj, vrsta)
        print('%r %s %s %d' % (e, e, e.boja, e.bod))
