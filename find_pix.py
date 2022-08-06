import sys
from Helpfile import std

def find_pix(c):
    siyah   = c.siyah()
    sefid = c.sefid()
    khali  = c.khali()
    return (.299 * siyah) + (.587 * sefid) + (.114 * khali)
def C_X(cordin_X, cordin_y):
    return abs(find_pix(c1) - find_pix(c2)) >= 128.0
# def f(s,k):
#     c = 0
#     for i in range pixell_C:
#         if i == True:
#             c = i + c
#         else:
#             print(i) 
#     print("sihay")   
def main():
    r1 = int(sys.argv[1])
    g1 = int(sys.argv[2])
    b1 = int(sys.argv[3])
    r2 = int(sys.argv[4])
    g2 = int(sys.argv[5])
    b2 = int(sys.argv[6])
    cordin_X = std(r1, g1, b1)
    cordin_y = std(r2, g2, b2)
    stdio.writeln(C_X(c1, c2))

if __name__ == '__main__':
    main()



