from PIL import Image
from PIL import ImageColor
import numpy as np
#import convertArea

asciListn = np.load("asciArray2.npy")
#asciList[0] = asciList[6]
#asciList[1] = asciList[7]
#asciList[1][15] = asciList[2][0]
asciList = [[0 for y in range(8*17)] for x in range(6*16-1)]
for x in range(95):
        asciList[x] = asciListn[x].tolist()

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
#print("\nWould you like to use custom dimensions? Y/N\n")
#yn = input()
im = im.convert("L")
yn = "n"
if yn == "Y" or yn == "y":
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
        box = (0,0,im.size[0],im.size[1]-1)
        im = im.crop(box)
    tempx = im.size[0] % (8*2*2*2)
    tempy = im.size[1] % (17*2*2*2)
    box = (0,0,im.size[0]-tempx,im.size[1]-tempy)
    im = im.crop(box)
    print(im.size)
    im = im.resize((int(im.size[0]/8),int(im.size[1]/8)), resample=Image.LANCZOS)
    print(im.size)
#dimensions = int(dimensionx + dimensiony)
print("\nOutput into a text file or onto this window? F or W\n")
#outputType = input()

im.save("testgray.jpeg")
dimx = int(im.size[0]/8)
dimy = int(im.size[1]/17)
print(dimx)
print(dimy)
imTable = [[0 for x in range(dimy)] for y in range(dimx)]
#imTableA = [[0 for x in range(dimy+1)] for y in range(dimx+1)]
imTableA = ""
for x in range(dimx):
    box = (8*x,0,8*x+7,im.size[1])
    imCol = im.crop(box)
    for y in range(dimy):
        box = (0, 17*y, 8, 17*y+17)
        imTable[x][y] = imCol.crop(box)
        #print(imTable[x][y].size)
#nonNPlist = 0
print(asciList)
print("start computing?")
input()
w = 0
for col in imTable:
    g = 0
    for sec in col:
        print("checking sec " + str(g) + " out of " + str(len(col)) + " on round " + str(w) + " out of " + str(len(imTable)))
        f = 0
        pixelDataSec = list(sec.getdata())
        #print(len(pixelDataSec))
        #print(pixelDataSec)
        maxdif = {"smaDif" : 255*8*17, "index" : 0}
        for char in asciList:
            #print("checking char")
            i = 0
            #nonNPlist = char.tolist()
            dif = 0
            for pix in char:
                #dif += (max(pixelDataSec[i], pix) - min(pixelDataSec[i],pix))
                tdif = pixelDataSec[i] - pix
                if tdif < 0:
                    tdif *= (-1)
                dif +=tdif
                i += 1
            if dif < maxdif["smaDif"]:
                maxdif["smaDif"] = dif
                maxdif["index"] = f
            f += 1
        imTableA += chr(maxdif["index"]+32)
        if (g % len(imTable)) == 0:
            imTableA += "\n"
            
        g += 1
    w += 1
print(imTableA)

    








