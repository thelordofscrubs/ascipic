from PIL import Image



def convertToAscChar(gsi):
    w, h = gsi.size
    pixelsx = []
    for a in range(h):
        for b in range(w):
            pixelsx[a][b] = gsi.getpixel(b,a)


def findClosestChar():

