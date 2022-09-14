import numpy as np
from keras.utils import load_img
from keras.utils import img_to_array
import matplotlib.pyplot as plt

def generateFile(array):
    file = open("./static/level1.txt", "w")
    for row in array:
        for pix in row:
            file.write(str(row[pix]) + " ")
        file.write("\n\n")
    file.close()

def coloravg(array):
    #red = 0
    #green = 0
    #blue = 0
    color = 0
    rown, coln, chan = np.shape(array)
    n = rown * coln

    for row in array:
        for pix in range(len(row)):
            color += row[pix][0]
            #red += row[pix][0]
            #green += row[pix][1]
            #blue += row[pix][2]
    #red = int(red / n)
    #green = int(green / n)
    #blue = int(blue / n)
    #return red, green, blue
    return color/n

def listColors():
    file = open("./static/colors2.txt", "w")
    for i in range(3, 14):
        for j in range(1, 9):
            img = load_img("./static/tile" + str(i) + "-" + str(j) + ".png", color_mode="grayscale")
            img_array = img_to_array(img)
            #print(img_array[0])
            color = coloravg(img_array)
            #file.write("tile " + str(i) + "-" + str(j) + ": " + str(r) + " " + str(g) + " " + str(b) + "\n")
            #file.write("tile " + str(i) + "-" + str(j) + ": " + str(color) + "\n")
            file.write(str(color) + "\n")
    file.close()


#listColors()
img = load_img("./static/tile7-2.png", color_mode="grayscale")
img_array = img_to_array(img)

histogram, bin_edges = np.histogram(img_array, bins=256)
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()
