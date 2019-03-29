from PIL import Image
import numpy as np

pic = "acscon2.jpeg"
im = Image.open(pic)
print(im.format, im.size, im.mode,)
#im = im.point(lambda p : p > 128 and 255)
#im.save("acscon3.jpeg")
#box = (18, 18, 357, 357)
#newpic = im.crop(box)
#newpic = newpic.convert("1")
#plut = []
#for w in range(3)
#    for i in range(256)
#        if i == 0:
#            plut.append(0)
#        elif:
#            plut.append(1)


#newpic1 = newpic.convert("1","NONE")
#print(newpic1.format, newpic1.size, newpic1.mode,)
#newpic1.save("acscon2.jpg")
#new = im.convert("1")
#new.save("acscon1.jpeg")
imgTable = [[0 for x in range(16)] for y in range(16)]
for i in range(16):
    for f in range(16):
        box = ((7+21*f),(4+21*i),(15+21*f),(21+21*i))
        imgTable[i][f] = im.crop(box)
        #imgTable[i][f].save("imgTable["+str(i)+"]["+str(f)+"].jpeg")
imgTable[0][8] = imgTable[0][0]
imgTable[0][10] = imgTable[0][0]
imgTable[11][2] = imgTable[0][0]
imgTable[13][11] = imgTable[0][0]
pixelArray = []
#imgTable [3][5] = imgTable[3][5].point(lambda p: p > 128 and 255)
#print(list(imgTable[3][5].getdata()))
for x in range(16):
    for y in range(16):
        imgTable[x][y] = imgTable[x][y].point(lambda p: p > 128 and 255)
        pixelArray.append(list(imgTable[x][y].getdata()))
#        print(pixelArray[x][y])
finalArray = np.array(pixelArray)
#print(finalArray)
np.save("asciArray.npy",finalArray)
        