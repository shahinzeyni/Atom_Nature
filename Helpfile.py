import sys
class std:
    def __init__(self, r=0, g=0, b=0):
        self._r = r  
        self._g = g  
        self._b = b  
    def siyah(self):
        return self._r
    def sefid(self):
        return self._g
    def khali(self):
        return self._b
    def __str__(self):
        return '(' + str(self._r) + ', ' + str(self._g) + ', ' + str(self._b) + ')'
sefidd = std(255, 255, 255)
siyahh = std(  0,   0,   0)
def _main():    
   
    c1 = std(128, 128, 128)
    # stdioo.writeln(c1)
    # stdioo.writeln(c1.siyah())
    # stdioo.writeln(c1.sefid())
    # stdioo.writeln(c1.khali())
if __name__ == '__main__':
    _main()
def pio(c1, c2):
    return abs(find_pix(c1) - find_pix(c2)) >= 128.0
def main():
    r1 = int(sys.argv[1])
    g1 = int(sys.argv[2])
    b1 = int(sys.argv[3])
    r2 = int(sys.argv[4])
    g2 = int(sys.argv[5])
    b2 = int(sys.argv[6])
    c1 = std(r1, g1, b1)
    c2 = std(r2, g2, b2)
    # stdioo.writeln(pio(c1, c2))
if __name__ == '__main__':
    main()




