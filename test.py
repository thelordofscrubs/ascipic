import numpy as np

npyArray = np.load("asciArray.npy")
i = 0
f = 0
line = ""
'''
for array in npyArray:
    for character in array:
        if character == 255:
            line += str(1)
        elif character == 0:
            line += str(0)
        if i == 8:
            line += "\n"
            i = 0
            f += 1
        i += 1
        if f == 17:
            line+="\n\n"
            f = 0
    print(line)
'''
for x in range(32):
    for y in range(17):
        for z in range(8):
            for char in npyArray[x*z][y*8:(y+1)*8]:
                if char == 255:
                    line += "1"
                else:
                    line += "0"
            line += "  "
        line += "\n"
    line += "\n"
    i += 1
print(line)