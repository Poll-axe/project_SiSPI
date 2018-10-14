import numpy

from skimage import img_as_float
from skimage.io import imread, imsave
from numpy import dstack

# считывание и получение информации
img = imread('03.png')
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

# обрезка по крааям
b = b[int(hm*0.10):int(hm*0.90), int(wm*0.10):int(wm*0.90)]
g = g[int(hm*0.10):int(hm*0.90), int(wm*0.10):int(wm*0.90)]
r = r[int(hm*0.10):int(hm*0.90), int(wm*0.10):int(wm*0.90)]

# совмещение на пофиг
img_comin = dstack((r, g, b))
imsave('out_img.png', img_comin)

# совмещение с учётом корреляции

# синий и зелёный
cor = 0
iib = 0
jjb = 0
bc = b.copy()
bc2 = b.copy()
bc3 = b.copy()
for i in range(-15, 15):
    bc = numpy.roll(bc, i, 0)
    for j in range(-15, 15):
        bc = numpy.roll(bc, j, 1)
        corij = (bc*g).sum()
        if corij >= cor:
            iib = i
            jjb = j
            cor = corij
    bc = bc2
print(iib, jjb)
b = numpy.roll(b, iib, 0)
b = numpy.roll(b, jjb, 1)
imsave('b_obr2.png', b)

# красный и зелёный
cor = 0
iir = 0
jjr = 0
rc = r.copy()
rc2 = r.copy()
rc3 = r.copy()
for i in range(-15, 15):
    rc = numpy.roll(rc, i, 0)
    for j in range(-15, 15):
        rc = numpy.roll(rc, j, 1)
        corij = (rc*g).sum()
        if corij >= cor:
            iir = i
            jjr = j
            cor = corij
    rc = rc2
print(iir, jjr)
r = numpy.roll(r, iir, 0)
r = numpy.roll(r, jjr, 1)
imsave('r_obr2.png', r)


img_comin = dstack((r, g, b))
imsave('out_img2.png', img_comin)