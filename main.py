from PIL import Image
from PIL import ImageColor
import numpy as np
#import convertArea

print("please input the file name\n(This program was written to work with PNG and JPEG, but may work with others)")
sI = input()
print("\nWould you like to use custom dimensions? Y/N\n")
if input() == "Y" or input() == "y":
    cd = True
else:
    cd = False
if cd:
    print("\nplease input the x dimension of the ASCII picture you want\n")
    dimensionx = input()
    print("\nplease input the y dimension of the ASCII picture you want\n")
    dimensiony = input()
else:
    if sI.size[0]%2:
        box = (0,0,sI.size[0]-1,sI.size[1])
        sI = sI.crop(box)
    if sI.size[1]%2:
        box = (0,0,sI.size[0],sI.size[1]-1)
        sI = sI.crop(box)
    tempx = sI.size[0]/16
    tempy = sI.size[1]/34
#dimensions = int(dimensionx . dimensiony)
print("\nOutput into a text file or onto this window? F or W\n")
outputType = input()
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
gi = im.convert("L")
#gi.save("testgray.jpeg")





