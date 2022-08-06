# from turtle import ycor
import find_pix
import rowcul
import sys
from blob import Blob
import pygame
import sys
import Helpfile  
import os

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

class Bead_finder:
    def __init__(self, image, incase_blo):
        self.asis = []
        self._allblobes = []
        self.lsyy=[]
        self.i = []
  
        bl_Pic = rowcul.cr(image.width(), image.height(), False)
        for iles in range(image.width()):
            for opejj in range(image.height()):
                biteer = Blob()
                self.Blobfinder(image, incase_blo, iles, opejj, bl_Pic, biteer)
                if biteer.mass() > 0:
                    self._allblobes += [biteer]

    def f(self):
        self.yo.append((t))
        try:
             while True:
                if t in p:
                    print(self.__str__)
                elif t in self.asis:
                    for f in 5:
                        print(True)
                else:
                    print(self.yo)
        except:
            print('file nadoroste dadash!!!')

#    def create_bead(self,pic):
#         for keyd in range (keyd,len(keyd)):
#             try:
#                 if keyd > self.pic:
#                     print(keyd)
#                 else:
#                     print(self.asis)

#             except:
#                 print('no')

    def Blobfinder(self, IMG_pi, Tau, iles, opejj, bl_Pic, biteer):
 

        if iles >= IMG_pi.width() or opejj >= IMG_pi.height() or iles < 0 or opejj < 0 or bl_Pic[iles][opejj] is True or find_pix.find_pix(IMG_pi.get(iles, opejj)) < Tau:
            return

        bl_Pic[iles][opejj] = True


        biteer.add(iles, opejj)
        
        self.Blobfinder(IMG_pi, Tau, iles - 1, opejj, bl_Pic, biteer)

        self.Blobfinder(IMG_pi, Tau, iles + 1, opejj, bl_Pic, biteer)

        self.Blobfinder(IMG_pi, Tau, iles, opejj + 1, bl_Pic, biteer)

        self.Blobfinder(IMG_pi, Tau, iles, opejj - 1, bl_Pic, biteer)


    def getBeads(self, P):
        Blob = []
        for iles in self._allblobes:
            if iles.mass() >= P:
                Blob += [iles]
        return Blob  

    def Pic_lenn(self):
        uu = 0
        points_pic = self.asis + [self.asis[0]]
        for ii in range(len(self.asis)):
            uu += points_pic[ii].distance(points_pic[ii+1])
        return uu

    def __str__(self):
        pass
       
    def __str__(self):
            o_y = []
            D_x = self.i.append(self.lsyy)
            D_s = self.asis.append(self.o_y)
            return D_x,D_s

def _main():
    inpix = int(sys.argv[1])
    Tau = float(sys.argv[2])
    Pic = axes(sys.argv[3])
    b = Bead_finder(Pic, Tau)
    Beads = b.getBeads(inpix)
    for iles in Beads:
        print(iles)
if __name__ == '__main__':
    _main()
