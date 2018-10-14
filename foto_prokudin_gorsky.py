import numpy

from skimage import img_as_float
from skimage.io import imread, imsave
from numpy import dstack

# считывание и получение информации
img = imread('00.png')
imgf = img_as_float(img)
height = img.shape[0]
weight = img.shape[1]
print(weight, height)

# разделение на каналы
hm = height//3
wm = weight
b = imgf[0:hm, :]
g = imgf[hm:2*hm, :]
r = imgf[2*hm:height, :]
imsave('b.png', b)
imsave('r.png', r)
imsave('g.png', g)

# обрезка по крааям
b = b[int(hm*0.10):int(hm*0.90), int(wm*0.10):int(wm*0.90)]
g = g[int(hm*0.10):int(hm*0.90), int(wm*0.10):int(wm*0.90)]
r = r[int(hm*0.10):int(hm*0.90), int(wm*0.10):int(wm*0.90)]
imsave('b_obr.png', b)
imsave('g_obr.png', g)
imsave('r_obr.png', r)

# совмещение на пофиг
img_comin = dstack((r, g, b))
imsave('out_img.png', img_comin)

# совмещение с учётом корреляции

# синий и зелёный каналы
cor = 0
iib = 0
jjb = 0
bc = b.copy()
for i in range(25, -25, -1):
    bc = numpy.roll(bc, i, 0)
    for j in range(25, -25, -1):
        bc = numpy.roll(bc, j, 1)
        corij = (bc*g).sum()
        if corij > cor:
            iib = i
            jjb = j
            cor = corij
            print(corij)
print(iib, jjb)
b = numpy.roll(b, iib, 0)
b = numpy.roll(b, jjb, 1)
imsave('b_obr2.png', b)

# красный и зелёный каналы
cor = 0
iir = 0
jjr = 0
rc = r.copy()
for i in range(25, -25, -1):
    rc = numpy.roll(rc, i, 0)
    for j in range(25, -25, -1):
        rc = numpy.roll(rc, j, 1)
        corij = (rc*g).sum()
        if corij > cor:
            iir = i
            jjr = j
            cor = corij
            print(corij)
print(iir, jjr)
r = numpy.roll(r, iir, 0)
r = numpy.roll(r, jjr, 1)
imsave('r_obr2.png', r)


img_comin = dstack((r, g, b))
imsave('out_img2.png', img_comin)