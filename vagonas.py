class Vagonas:

    def __init__(self, mase, didMase, ID):
        self.ID = ID
        self.mase = mase
        self.didMase = didMase
        self.dabarMase = 0

    def __str__(self):
        return "ID = %s, mase  = %s, maksimali mase= %s, mase kroviniu = %s" % (self.ID,
                                                                        self.mase,
                                                                        self.didMase,
                                                                        self.dabarMase )
    def addKrovinys(self, krovMase):
        if self.didMase >= krovMase + self.dabarMase:
            self.dabarMase += krovMase
            return True
        return False

    def getVagMase(self):
        return self.mase

    def getVagMaxMase(self):
        return self.didMase

    def getVagId(self):
        return self.ID

    def getVagMaseKroviniu(self):
        return self.dabarMase

    def setMasKrov(self, mase):
        self.Dabarmase = mase

    def getVagonasLaisvaMase(self):
        return self.didMase - self.dabarMase

    def __repr__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return self.name

    def __len__(self,):
        return self._len__

    def get_id(self):
        return id
