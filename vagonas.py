import doctest
class Vagonas:

    def __init__(self, mase, didMase, ID):
        """test init
	>>> a = Vagonas(100,1200,011)
        >>> print(a)
        ID = 500, mase  = 100, maksimali mase= 1200, mase kroviniu = 0
        >>> a.get_vag_id()
        011
        >>> a.get_vag_mase()
        100
        >>> a.get_did_mase()
        1200
        >>> a.krov_mase()
        0
	"""
        self.ID = ID
        self.mase = mase
        self.didMase = didMase
        self.dabarMase = 0

    def __str__(self):
        return "ID = %s, mase  = %s, maksimali mase= %s, mase kroviniu = %s" % (self.ID,
                                                                        self.mase,
                                                                        self.didMase,
                                                                        self.dabarMase)
    def add_krov(self, krovMase):
        if self.didMase >= krovMase + self.dabarMase:
            self.dabarMase += krovMase
            return True
        return False

    def get_vag_mase(self):
        return self.mase

    def get_did_mase(self):
        return self.didMase

    def get_vag_id(self):
        return self.ID

    def krov_mase(self):
        return self.dabarMase

    def set_mas_krov(self, mase):
        self.dabarMase = mase

    def get_vag_laisva_mase(self):
        return self.didMase - self.dabarMase

    def __repr__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return self.name

    def __len__(self,):
        return self._len__

    def get_id(self):
        return id

if __name__ == "__main__":
	doctest.testmod()
