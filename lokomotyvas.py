import doctest
class Lokomotyvas:

    def __init__(self, name, mase, didTemp):
        self.name = name
        self.mase = mase
        self.didTemp = didTemp

    def __sub__(a, b):
        return a - b

    def getLokMase(self):
        return self.mase

    def getLokGalia(self):
        return self.didTemp

    def getLokName(self):
        return self.name

    def __repr__(self):
        return "%s" % (self.name)

    def __str__(self):
        return "Lokomotyvas = %s  Mase = %s, tempiamoji galia = %s" % (self.name, self.mase, self.didTemp)

if __name__ == "__main__":
	doctest.testmod()
