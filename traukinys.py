from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import codecs
import doctest

class Traukinys():

    def __init__(self, name):
        """test init
    >>> a = Traukinys("Third Reich")

        >>> print(a)
        Traukinys: Traukinys, visa masė: 140,
                   traukinio galia: 500, visa krovinio mase 0
                   lokomotyvų skaičius = 1, vagonų skaičius = 1

        >>> a.add_lok("Berlin ",100,500)
        lokomotyvas sekmingai pridetas

        >>> a.add_vag(350, 40,500)
        vagonas sekmingai pridetas

        >>> print(a)
        traukinys: Traukinys, Dabartine sastato mase: 140,
                   galia: 500, bendra kroviniu mase 0
                   lokomotyvu = 1, vagonu = 1

        >>> a.pakrauti_krovini(100)
        pavyko prideti krovini i vagons1 dar liko 400 vietos siame vagone

      """
        self.nameTraukinys = name
        self.lokomotyvas = []
        self.vagonas = []
        self.kroviniuMase = 0
        self.tempGalia = 0
        self.visaMase = 0


    def jdefault(o):
        if isinstance(o, set):
            return list(o)
        return o.__dict__

    def add_lok(self, name, mase, didTemp):
        if didTemp >= mase:
            self.lokomotyvas.append(Lokomotyvas(name, mase, didTemp))
            self.tempGalia += didTemp
            self.visaMase += mase
            print("Lokomotyvas pridėtas")
        else:
            return print("Lokomotyvo tempimo galia maženė už jo paties masę, lokomotyvas nepridėtas ")

    def add_vag(self, ID, mase, didMase):
        if self.tempGalia < self.visaMase + mase:
            return print("Vagonas neprikabintas, lokomotyvai nebegali daugiau patempti vagonų")
        else:
            self.vagonas.append(Vagonas(mase, didMase, ID))
            self.visaMase += mase
            print("Vagonas prikabintas")

    def set_train_stats(self, mase, krovMase, galia):
        self.kroviniuMase = krovMase
        self.tempGalia = galia
        self.visaMase = mase

    def get_train_galia(self):
        return print("Traukinio tempimo galia: %s" % (self.tempGalia))

    def get_train_temp(self):
        return self.tempGalia

    def visa_mase(self):
        return self.visaMase

    def get_all_krov_mase(self):
        return self.kroviniuMase

    def get_lokomotyvas(self):
        return self.lokomotyvas

    def get_vagonas(self):
        return self.vagonas

    def get_train_name(self):
        return self.nameTraukinys

    def __str__(self):
        return """Traukinys: %s, visa masė: %s,
                   traukinio galia: %s, visa krovinio mase %s
                   lokomotyvų skaičius = %s, vagonų skaičius = %s """ % (self.nameTraukinys,
                                                                         self.visaMase,
                                                                         self.tempGalia,
                                                                         self.kroviniuMase,
                                                                         len(self.lokomotyvas),
                                                                         len(self.vagonas))

    def __repr__(self):
        return "<%s>" % (self.nameTraukinys)

    def pakrauti_krovini(self, masKrov):
        if self.tempGalia < self.visaMase + masKrov:
            return print("krovinio masė viršija traukinio pajėgumus, krovinys nepridėtas")
        else:
            for vagonas in self.vagonas:
                a = vagonas.addKrovinys(masKrov)
                if a == False:
                    continue
                else:
                    self.visaMase += masKrov
                    self.kroviniuMase += masKrov
                    if vagonas.getVagonasLaisvaMase() == 0:
                        return print("Krovinys pridėtas, vagonas %s pilnas" % (vagonas.getVagId()))
                    else:
                        return print("Krovinys pridėtas %s, laisvos vietos liko: %s " % (vagonas.getVagId(),
                                                                                         vagonas.getVagonasLaisvaMase()))
            return print("Krovinys nepridėtas, neužtenka vietos")


def issaugoti(sarasas):
    with open('trauk_sąrašas.json', 'w') as fp:
        lok_listas = []
        for trauk in range(0, len(sarasas)):
            traukinys = sarasas[trauk-1]
            if(traukinys.lokomotyvas != 0):
                for i in range(0, len(traukinys.lokomotyvas)):
                    lokomotyvai = {}
                    lokomotyvai = {
                        "lokomotyvas": traukinys.lokomotyvas[i].getLokName(),
                        "mase": traukinys.lokomotyvas[i].getLokMase(),
                        "galia": traukinys.lokomotyvas[i].getLokGalia()}
                lok_listas.append(lokomotyvai)

            if(traukinys.vagonas != 0):
                vag_listas = []
                for j in range(0, len(traukinys.vagonas)):
                    vagonai = {}
                    vagonai = {
                        "ID": traukinys.vagonas[j].getVagId(),
                        "mase": traukinys.vagonas[j].getVagMase(),
                        "max_mase": traukinys.vagonas[j].getVagMaxMase(),
                        "kroviniu_mase": traukinys.vagonas[j].getVagMaseKroviniu()}
                vag_listas.append(vagonai)

            traukiniai = {
                "Pavadinimas": traukinys.nameTraukinys,
                "visa kroviniu mase": traukinys.kroviniuMase,
                "galia": traukinys.tempGalia,
                "visa traukinio mase": traukinys.visaMase,
                "lokomotyvai": lok_listas,
                "vagonai": vag_listas
            }
            json.dump(traukiniai, fp)
            fp.write("\n")
    fp.close()

    def __sub__(a, b):
        return a - b


def skaityti():
    data = []
    return_listas = []
    with open('trauk_sąrašas.json', 'r') as failas:
        for i in failas:
            data.append(json.loads(i))

        for item in data:
            new_train = Traukinys(item["Pavadinimas"])
            new_train.add_lok(item["visa traukinio mase"],
                                    item["visa kroviniu mase"],
                                    item["galia"])
            for j in item["vagonai"]:
                temp_vagonas = Vagonas(j["ID"], j["mase"],
                                       j["max_mase"])
                temp_vagonas.set_mas_krov(j["kroviniu_mase"])
                new_train.vagonas.append(temp_vagonas)

            for z in item["lokomotyvai"]:
                temp_lokomotyvas = Lokomotyvas(z["lokomotyvas"], z["mase"],
                                               z["galia"])
                new_train.lokomotyvas.append(temp_lokomotyvas)
            return_listas.append(new_train)
        return return_listas


    def __len__(self,):
        return self._len__

    def get_id(self):
        return id

    if __name__ == "__main__":
    	doctest.testmod()
