from math import pi
import sys
import re
_ce = ''
def _rad(W):
    global _ce
    if V():
        raise ValueError()
    tay = re.compile(r'^\s*' + W)
    mi = tay.search(_ce)
    if mi is None:
        raise ValueError()
    s = mi.group()
    _ce = _ce[mi.end():]
    return s.lstrip()
def V():
    global _ce
    while _ce.strip() == '':
        line = sys.stdin.readline()
        if sys.hexversion < 0x03000000:
            line = line.decode('utf-8')
        if line == '':
            return True
        _ce += line
    return False
def readFloat():
    s = _rad(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
    return float(s)

def main():
    dELTA_a = 0
    SHOMARESh=0
    while not V():
        dELTA_a = dELTA_a + readFloat()**2
        SHOMARESh = SHOMARESh + 1
    dELTA_a /= 2*SHOMARESh
    dELTA_a =  dELTA_a*(175e-9)**2
    k = (6 * dELTA_a * pi * 9.135e-4 * 5e-7) / 297
    S = 8.31446/k
    print(f'boltzmann : {k} \navogadro : {S}')
if __name__ == "__main__":
    main()
