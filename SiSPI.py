import matplotlib.pyplot as pyp
import numpy as np
from pandas import Series, qcut
import statistics as stat
import skimage
from skimage import img_as_float
from skimage.io import imread


def spectr_razlozh(flat_array, name_title):
    ts = Series(flat_array)
    ts.plot(kind='kde', title=name_title)

    pyp.show()
    pyp.title(name_title)
    pyp.hist(flat_array, 100)
    pyp.show()


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
flat_gray = gray.ravel()
truegrey = skimage.color.rgb2grey(imgf)
"""

print('ME red specter = ', stat.mean(flat_red))
print('Dispersia red spectr = ', stat.variance(flat_red))
print('ME green specter = ', stat.mean(flat_green))
print('Dispersia green spectr = ', stat.variance(flat_green))
print('ME blue specter = ', stat.mean(flat_blue))
print('Dispersia blue spectr = ', stat.variance(flat_blue))
print('Cov matrix')
print(np.cov([flat_red, flat_green, flat_blue]))
"""
spectr_razlozh(flat_red, 'red spectr')
spectr_razlozh(flat_green, 'green spectr')
spectr_razlozh(flat_blue, 'blue spectr')
print('ME brightness = ', stat.mean(flat_gray))
print('Dispersia brightness = ', stat.variance(flat_gray))
spectr_razlozh(flat_gray, 'Brightness spectr')

