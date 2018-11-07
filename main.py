import statistics
import skimage
from PIL import Image, ImageDraw
import numpy
from skimage import img_as_float
from skimage.io import imread, imsave

# import functions


# считывание и получение информации
img = imread('file.jpg')
imgf = img_as_float(img)
height = img.shape[0]
weight = img.shape[1]

# получение каналов изображения
red = imgf[:, :, 0]
green = imgf[:, :, 1]
blue = imgf[:, :, 2]

# получение яркости изображения
gray = (red + green + blue) / 3
truegrey = skimage.color.rgb2grey(imgf)

odnom = red.ravel()
print(statistics.mean(odnom))
