import random
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.

image = Image.open("file.JPG")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.

for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        draw.point((i, j), (255 - a, 255 - b, 255 - c))
image.save("ans.jpg", "JPEG")
del draw
