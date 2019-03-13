from PIL import Image

print("please input the file name\n(This program was written to work with PNG and JPEG, but may work with others)")
startingImage = input()
print("please input the x dimension of the ASCII picture you want")
dimensionx = input()
print("please input the y dimension of the ASCII picture you want")
dimensiony = input()
dimensions = int(dimensionx . dimensiony)
print("Output into a text file or onto this window? F or W")
outputType = input()
try:
    im = Image.open(startingImage)
except IOError:
    print("that file can't be opened")
    exit
im.convert




