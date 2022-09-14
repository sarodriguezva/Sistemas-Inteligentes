from math import ceil
from math import floor
from keras.utils import load_img
from keras.utils import img_to_array
from keras.utils import array_to_img

img = load_img("./static/level1.png", color_mode="grayscale")
img_array = img_to_array(img)

ts = 43.8   #Tile size
fr = 3      #First row
lr = 14     #Last row
fc = 1      #First column
lc = 9      #Last column

#Región Jugable
region = img_array[ceil(ts*fr):floor(ts*lr), ceil(ts*fc):floor(ts*lc)]
region_img = array_to_img(region)
region_img.save("./static/level1_cutgs.png")


def generateTiles():
    for i in range(3, 14):
        for j in range(1, 9):
            region = img_array[ceil(ts * i):floor(ts * (i+1)), ceil(ts * j):floor(ts * (j+1))]
            region_img = array_to_img(region)
            region_img.save("tile" + str(i) + "-" + str(j) + ".png")

#3-4 4-5 5-6 6-7 7-8 8-9 9-10 10-11 11-12 12-13 13-14 ROWS
#1-2 2-3 3-4 4-5 5-6 6-7 7-8 8-9 COLUMNS
