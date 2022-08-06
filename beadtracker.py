import sys
import pygame
from beadfinder import Bead_finder
import Helpfile
import glob
import sys
import pygame
import sys
import re
# import os

_pix1 = 512
_pix2 = 512

class axes:
    def __init__(self, X_s=None, Y_s=None):
        if (X_s is not None) and (Y_s is None):
            fileName = X_s
            try:
                self._surface = pygame.image.load(fileName)
            except pygame.error:
                pass

    def width(self):
        return self._surface.get_width()
    def height(self):
        return self._surface.get_height()

    def get(self, x, y):
        pygameColor = self._surface.get_at((x, y))
        return Helpfile.std(pygameColor.r, pygameColor.g, pygameColor.b)


def isnumm(rotten=''):
    if sys.hexversion < 0x03000000:
        rotten = rotten.encode('utf-8')
    else:
        rotten = str(rotten)
    sys.stdout.write(rotten)
    sys.stdout.write('\n')
    sys.stdout.flush()

def isstrr(Qau, *sart):
    rotten = Qau % sart
    if sys.hexversion < 0x03000000:
        rotten = unicode(x)
        rotten = rotten.encode('utf-8')
    sys.stdout.write(rotten)
    sys.stdout.flush()

def main():
    MiN_pix= int(sys.argv[1])
    Tau = float(sys.argv[2]) 
    dilt = float(sys.argv[3])
    images = glob.glob(sys.argv[4])
    woper = Bead_finder(axes(images[0]), Tau)
    q_q = woper.getBeads(MiN_pix)
    for i in range(1, len(images)):
        woper = Bead_finder(axes(images[i]), Tau)
        bead = woper.getBeads(MiN_pix)
        for c_b in bead:
            distance_y = float('inf')
            for per in q_q:
                d = c_b.distance(per)
                if d <= dilt and d < distance_y:
                    distance_y = d
            if distance_y != float('inf'):
                isstrr('%.4f\n', distance_y)
        isnumm()
        q_q = bead

if __name__ == '__main__':
    main()
