from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
from traukinys import Traukinys, Skaityti, Issaugoti
import doctest

def Meniu():
    """test init

        >>> 1
        >>> 1

    """
    ats = True
    sarasas = Skaityti()
    if len(sarasas) > 0:
        traukinys = sarasas[0]
    else:
        traukinys = None

    def pasirinkimas1(ats):
        if sarasas == []:
            print("nėra traukinių")
            return ats == True

        #rikiavimas(sarasas)

        print("Traukiniu sąrašas: \n")
        for i in range(0, len(sarasas)):
            print (i+1, '-', sarasas[i].nameTraukinys)

        return pasirinkimas11(sarasas, ats)

    def rikiavimas(sarasas):
        print("Jei nori išrikiuoti (pagal) - spausk: (Galingumą) - G, (Mase) - M, (Krovinius) - K")
        try:
            pas = str(input())
            if (pas == 'G'):
                def galiaTrauk(sarasas):
                    return traukinys.tempGalia
                print(sorted(sarasas, key=galiaTrauk))
            if (pas == 'M'):
                def maseTrauk(sarasas):
                    return traukinys.visaMase
                print(sorted(sarasas, key=maseTrauk))
            if (pas == 'K'):
                def bendraKrovMaseTrauk(sarasas):
                    return traukinys.kroviniuMase
                print(sorted(sarasas, key=bendraKrovMaseTrauk))
        except ValueError:
            print("bloga ivestis")

    def pasirinkimas11(sarasas, ats):
        print("Pasirinkti traukinį - eilės nr. Atgal - 0")
        try:
            pas = int(input())
            if (pas > 0 and pas <= len(sarasas)):
                return pasirinkimas111(sarasas, ats, pas)
            elif (pas == 0):
                return pasirinkimas1
        except ValueError:
            print("bloga įvestis")

    def pasirinkimas111(sarasas, ats, pas):
        traukinys = sarasas[pas-1]
        print("Traukinys:", traukinys.nameTraukinys)

        if(traukinys.lokomotyvas != None):
            print("Lokomotyvai: ", len(traukinys.lokomotyvas))
            for i in range(0, len(traukinys.lokomotyvas)):
                print (traukinys.lokomotyvas[i])
        else:
            print("Lokomotyvų nėra")

        if(traukinys.vagonas != None):
            print("Vagonai: ", len(traukinys.vagonas))
            for i in range(0, len(traukinys.vagonas)):
                print (traukinys.vagonas[i])
        else:
            print("Vagonų nėra")

        print("Kroviniu svoris: ", traukinys.kroviniuMase)
        print("Traukinio galia: ", traukinys.tempGalia)
        print("Traukinio bendras svoris:", traukinys.visaMase)

        return kitasMeniu(traukinys, pas)

    def pasirinkimas2(sarasas, traukinys, ats):
        try:
            print("koks bus jūsų traukinio pavadinimas?")
            vardas = input()
            a = Traukinys(vardas)
            sarasas.append(a)
            print("kiek lokomotyvu turės šis traukinys?")
            try:
                lokKiek = int(input())
                pasirinkimas21(sarasas, traukinys, lokKiek)
            except ValueError:
                print("bloga ivestis")
            print("kiek vagonų turės šis traukinys?")
            try:
                vagKiek = int(input())
                pasirinkimas22(sarasas, traukinys, vagKiek)
            except ValueError:
                print("bloga ivestis")

            return ats == True
        except ValueError:
            print("bloga įvestis")
            return ats == True

    def pasirinkimas21(sarasas, traukinys, i):
        traukinys = sarasas[len(sarasas)-1]
        for j in range(0, i):
            print("Lokomotyvo pavadinimas:")
            try:
                pavadinimas = input()
                print("Lokomotyvo mase: ")
                try:
                    mase = int(input())
                    print("Lokomotyvo galia:")
                    galia = int(input())
                    if mase <= 0 or galia < 0:
                        raise ValueError
                    traukinys.addLokomotyvas(pavadinimas, mase, galia)
                except ValueError:
                    print("bloga įvestis")
                    return ats == True
            except ValueError:
                print("bloga įvestis")
                return ats == True

    def pasirinkimas22(sarasas, traukinys, i):
        traukinys = sarasas[len(sarasas)-1]
        for j in range(0, i):
            print("Vagono ID:")
            try:
                ID = input()
                print("Vagono svoris: ")
                try:
                    svoris = int(input())
                    print("Didžiausia galima vagono mase:")
                    mase = int(input())
                    if svoris <= 0 or mase < 0:
                        raise ValueError
                    traukinys.addVagonas(ID, svoris, mase)
                except ValueError:
                    print("bloga įvestis")
                    return ats == True
            except ValueError:
                print("bloga įvestis")
                return ats == True

    def pidetiKrov(traukinys, pas):
        if(traukinys.vagonas == None):
            print("šis traukinys neturi vagonų")
            return pas == True
        print("Krovinio dydis:")
        try:
            krovinys = int(input())
            if krovinys < 0:
                raise ValueError
            traukinys.pakrautiKrovini(krovinys)
        except ValueError:
            print("bloga ivestis")
            return pas == True

    def pridetiVag(traukinys, pas):
        print("Vagono ID:")
        try:
            ID = input()
            print("Vagono svoris: ")
            try:
                svoris = int(input())
                print("Didžiausia galima vagono mase:")
                mase = int(input())
                if svoris <= 0 or mase < 0:
                    raise ValueError
                traukinys.addVagonas(ID, svoris, mase)
            except ValueError:
                print("bloga įvestis")
                return pas == True
        except ValueError:
            print("bloga įvestis")
            return pas == True

    def pridetiLok(traukinys, pas):
        print("Lokomotyvo pavadinimas:")
        try:
            pavadinimas = input()
            print("Lokomotyvo mase: ")
            try:
                mase = int(input())
                print("Lokomotyvo galia:")
                galia = int(input())
                if mase <= 0 or galia < 0:
                    raise ValueError
                traukinys.addLokomotyvas(pavadinimas, mase, galia)
            except ValueError:
                print("bloga įvestis")
                return ats == True
        except ValueError:
            print("bloga įvestis")
            return ats == True

    def istrintiTra(traukinys, pas):
        print(traukinys.nameTraukinys, "ištrintas")
        sarasas.remove(traukinys)


    def kitasMeniu(traukinys, i):
        pas = True
        print("\n --- Traukinio Meniu ---")
        print("1. Pridėti krovinį 2. Prideti vagonus 3. Prideti lokomotyvus 4. Ištrinti traukinį 0. Atgal")

        while pas:
            try:
                pas = int(input())

                if pas == 1:
                    pidetiKrov(traukinys, pas)
                elif pas == 0:
                    pas = False
                elif pas == 2:
                    pridetiVag(traukinys, pas)
                elif pas == 3:
                    pridetiLok(traukinys, pas)
                elif pas == 4:
                    istrintiTra(traukinys, pas)

            except ValueError:
                print("neteisingai įvestas pasirinkimas")

    while ats:

        print(
    """ \n --- Meniu --- \n
1. Traukinių sąrašas
2. Pridėti traukinį prie sąrašo
3. Išsaugoti traukinių sąrašą faile
0. Baigti darbą
    """)


        try:
            ats = int(input())

            if ats == 1:
                pasirinkimas1(ats)
            elif ats == 0:
                print("darbas baigtas")
                ats = False
            elif ats == 2:
                pasirinkimas2(sarasas, traukinys, ats)
            elif ats == 3:
                Issaugoti(sarasas)
                print("sąrašas išsaugotas")

        except ValueError:
            print("neteisingai įvestas pasirinkimas")





if __name__ == "__main__":
    #Meniu()
    doctest.testmod()
