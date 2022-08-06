import sys


class Blob:
    # create __init__ dunder  have 3 itemes
    def __init__(self):

        self._create = 0

        self.lst = []

        self._Pixel_Blob = 0

        self.ltt = []

        self._Pixel_2_Blob = 0

    #  create def add  >> to ag

    def add(self, pixel_X, pixel_Y):
        self._Pixel_Blob = ((self._Pixel_Blob) * (self._create) + (pixel_X)) / (self._create + 1)
        self._Pixel_2_Blob = ((self._Pixel_2_Blob) * (self._create) + (pixel_Y)) / (self._create + 1)
        self._create = self._create + 1

    # def mass >>>  to show  self._create 

    def mass(self):
        return self._create


    def mass_pixel(self,q):
        return self.lst


    # def distanceTo  >> for show  pixel x and y  in image in class Blob

    def distance(self, other):
        Pixel_right_1 = self._Pixel_Blob

        Pixel_left_1 = self._Pixel_2_Blob

        Pixel_right_2 = other._Pixel_Blob

        Pixel_left_2 = other._Pixel_2_Blob

        destroid_x = (Pixel_right_1 - Pixel_right_2) ** 2

        destroid_y = (Pixel_left_1 - Pixel_left_2) ** 2

        result_self = (destroid_x + destroid_y) ** 0.5

        return result_self

# for read file  we use __str__  metud and  show  zero point in range 3
    def __str__(self):
        return '%d (%.3f, %.3f)' % (self._create, self._Pixel_Blob, self._Pixel_2_Blob)



# class Funder_Blob:
#     def __init__(self) -> None:
#         self.pix_A = []
#     @staticmethod
#     def distraction(i):
#         while True:
#             summ = summ + i
#     def g_Blob(self,ku,su):
#         for pix in range (2,6):
#             if pix in self.lst:
#                 pass
#             else:
#                 pass
#     def f(self, percent):
#         pixi = int(2 * (1 + t))
#     def __repr__(self):
#         return'[ %s, %s]'
# ob = Blob()
# ob.add(1, 5)
# print(ob)
