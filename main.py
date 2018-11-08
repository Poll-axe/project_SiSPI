import statistics
import skimage
import matplotlib.pyplot
from PIL import Image, ImageDraw
import numpy
from skimage import img_as_float
from skimage.io import imread, imsave
import functions


# считывание и получение информации
img = imread('ans.jpg')
imgf = img_as_float(img)
height = img.shape[0]
weight = img.shape[1]

# получение каналов изображения
red = imgf[:, :, 0]
green = imgf[:, :, 1]
blue = imgf[:, :, 2]

# перевод канналов в одномерные массивы
flat_red = red.ravel()
flat_green = green.ravel()
flat_blue = blue.ravel()


# получение яркости изображения
gray = (red + green + blue) / 3
truegrey = skimage.color.rgb2grey(imgf)

print(statistics.mean(flat_red))
print(functions.mat(flat_red))
