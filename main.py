from PIL import Image
from PIL import ImageColor
import numpy as np
#import convertArea

print("please input the file name\n(This program was written to work with PNG and JPEG, but may work with others)")
sI = input()
try:
    im = Image.open(sI)
except IOError:
    print("that file can't be opened")
    input()
    exit
except:
    print("something went wrong with opening the file")
    input()
    exit
print("\nWould you like to use custom dimensions? Y/N\n")
if input() == "Y" or input() == "y":
    cd = True
    print("\nrecommended ratio is two x to one y\n")
else:
    cd = False
if cd:
    print("\nplease input the x dimension of the ASCII picture you want\n")
    dimensionx = input()
    print("\nplease input the y dimension of the ASCII picture you want\n")
    dimensiony = input()
else:
    if im.size[0]%2:
        box = (0,0,im.size[0]-1,im.size[1])
        im = im.crop(box)
    if im.size[1]%2:
        box = (0,0,sI.size[0],sI.size[1]-1)
        im = im.crop(box)
    tempx = im.size[0] % 16
    tempy = im.size[1] % 34
    box = (0,0,im.size[0]-tempx,im.size[1]-tempy)
    im = im.crop(box)
    im.resize((im.size[0]/2,im.size[1]/2), resample=PIL.Image.LANCZOS)
#dimensions = int(dimensionx + dimensiony)
print("\nOutput into a text file or onto this window? F or W\n")
outputType = input()
gi = im.convert("L")
#gi.save("testgray.jpeg")
dimx = gi.size[0]/8
dimy = gi.size[1]/17
imTable = [[0 for x in range(dimx)] for y in range(dimy)]
for x in range(dimx):
    box = (8*x,0,8*x+7,gi.size[1])
    imCol = gi.crop(box)
    for y in range(dimy):
        box = (0, 17*z, 7, 17*z+16)
        imTable[x][y] = imCol.crop(box)








