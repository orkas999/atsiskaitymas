import doctest
class Lokomotyvas:

    def __init__(self, name, mase, didTemp):
        """test init
    >>> a = Lokomotyvas("Third Reich",1500,9000)
        >>> print(a)
        Lokomotyvas = Third Reich  Mase = 1500, tempiamoji galia = 9000

        >>> a.getLokName()
        'Third Reich'
        >>> a.getLokMase()
        1500
        >>> a.getLokGalia()
        9000
        """

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
