import os

import matplotlib.pyplot as pyp
import numpy as np
from pandas import Series, qcut
import statistics as stat
import skimage
from skimage import img_as_float
from skimage.io import imread
import cv2


def resize(image, height, weight):
    """

    :return: изображение
    :param image: изображение для ресайза
    :param height:  высота
    :param weight: ширина
    """
    dim = (weight, int(height))
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def spectr_razlozh(flat_array, name_title, data):
    ts = Series(flat_array)
    pyp.ylim([0, 50])  # установка ограничений на ось у
    pyp.xlim([-0.2, 1.2])  # установка ограничений на ось х
    ts.plot(kind='kde', title=name_title)
    pyp.text(-0.1, 26, data)
    pyp.show()


def spectr_razlozh_for_two(flat_array1, flat_array2, name_title, data):
    ts1 = Series(flat_array1)
    ts2 = Series(flat_array2)
    pyp.ylim([0, 50])  # установка ограничений на ось у
    pyp.xlim([-0.2, 1.2])  # установка ограничений на ось х
    ts1.plot(kind='kde', title=name_title)
    ts2.plot(kind='kde')
    pyp.legend(('Изображение 1', 'Изображение 2'), loc='best')
    pyp.text(-0.1, 26, data)
    pyp.show()


def cut_image(img):
    print(img.shape)
    x = int(input('Введите координату х '))
    y = int(input('Введите координату y '))
    h = int(input('Введите высоту h '))
    w = int(input('Введите ширину w '))
    crop_img = img[y:y + h, x:x + w]
    return crop_img


def analyz(img):
    # считывание и получение информации
    imgf = img_as_float(img)
    pyp.subplot(231), pyp.imshow(img, 'gray'), pyp.title('Картинка')

    pyp.tick_params(axis='both', labelleft=False,
                    labelright=False, labelbottom=False)
    pyp.show()

    # получение каналов изображения
    red = imgf[:, :, 0]
    green = imgf[:, :, 1]
    blue = imgf[:, :, 2]

    # перевод канналов в одномерные массивы
    flat_red = red.ravel()
    flat_green = green.ravel()
    flat_blue = blue.ravel()

    # получение яркости изображения
    truegray = skimage.color.rgb2grey(imgf)
    flat_gray = truegray.ravel()
    MO_RED = round(stat.mean(flat_red), 4)
    D_RED = round(stat.variance(flat_red), 4)

    MO_GREEN = round(stat.mean(flat_green), 4)
    D_GREEN = round(stat.variance(flat_green), 4)

    MO_BLUE = round(stat.mean(flat_blue), 4)
    D_BLUE = round(stat.variance(flat_blue), 4)

    print('Мат ожидание красного спектра = ', MO_RED)
    print('Дисперсия красного спектра = ', D_RED)

    print('Мат ожидание зеленого спектра = ', MO_GREEN)
    print('Дисперсия красного спектра = ', D_GREEN)

    print('Мат ожидание синего спектра = ', MO_BLUE)
    print('Дисперсия синего спектра = ', D_BLUE)
    print('Cov matrix')

    COV_MATRIX = np.cov([flat_red, flat_green, flat_blue])
    for string in range(COV_MATRIX.__len__()):
        for item in range(COV_MATRIX[string].__len__()):
            COV_MATRIX[string][item].__round__(4)
            print("{0:.4f}".format(COV_MATRIX[string][item]), end='    ')
        print()

    data_red = "МО = " + str(MO_RED) + '\n' + 'Д = ' + str(D_RED)
    data_green = "МО = " + str(MO_GREEN) + '\n' + 'Д = ' + str(D_GREEN)
    data_blue = "МО = " + str(MO_BLUE) + '\n' + 'Д = ' + str(D_BLUE)
    spectr_razlozh(flat_red, 'Красный спектр', data_red)
    spectr_razlozh(flat_green, 'Зеленый спектр', data_green)
    spectr_razlozh(flat_blue, 'Синий спектр', data_blue)

    MO_BRIGHT = round(stat.mean(flat_gray), 4)
    D_BRIGHT = round(stat.variance(flat_gray), 4)
    print('Мат ожидание яркости = ', MO_BRIGHT)
    print('Дисперсия яркости = ', D_BRIGHT)
    data_bright = "МО = " + str(MO_BRIGHT) + '\n' + 'Д = ' + str(D_BRIGHT)
    spectr_razlozh(flat_gray, 'Спектр яркости', data_bright)


def sravn_analyz(img1, img2):
    # считывание и получение информации
    height1 = img1.shape[0]
    weight1 = img1.shape[1]

    height2 = img2.shape[0]
    weight2 = img2.shape[1]

    height = min(height1, height2)
    weight = min(weight1, weight2)

    img1 = resize(img1, height, weight)
    img2 = resize(img2, height, weight)

    imgf1 = img_as_float(img1)
    pyp.subplot(231), pyp.imshow(img1, 'gray'), pyp.title('Kартинка 1')

    pyp.tick_params(axis='both', labelleft=False,
                    labelright=False, labelbottom=False)
    pyp.savefig("C:\\Users\DellPC\Documents\\file.JPG",)
    pyp.show()

    # получение каналов изображения
    red1 = imgf1[:, :, 0]
    green1 = imgf1[:, :, 1]
    blue1 = imgf1[:, :, 2]

    # перевод канналов в одномерные массивы
    flat_red1 = red1.ravel()
    flat_green1 = green1.ravel()
    flat_blue1 = blue1.ravel()
    truegray1 = skimage.color.rgb2grey(imgf1)
    flat_gray1 = truegray1.ravel()

    imgf2 = img_as_float(img2)
    pyp.subplot(231), pyp.imshow(img2, 'gray'), pyp.title('Kартинка 2')

    pyp.tick_params(axis='both', labelleft=False,
                    labelright=False, labelbottom=False)
    pyp.show()

    # получение каналов изображения
    red2 = imgf2[:, :, 0]
    green2 = imgf2[:, :, 1]
    blue2 = imgf2[:, :, 2]

    # перевод канналов в одномерные массивы
    flat_red2 = red2.ravel()
    flat_green2 = green2.ravel()
    flat_blue2 = blue2.ravel()
    truegray2 = skimage.color.rgb2grey(imgf2)
    flat_gray2 = truegray2.ravel()

    # Вычисление данных
    MO_RED1 = round(stat.mean(flat_red1), 4)
    D_RED1 = round(stat.variance(flat_red1), 4)

    MO_GREEN1 = round(stat.mean(flat_green1), 4)
    D_GREEN1 = round(stat.variance(flat_green1), 4)

    MO_BLUE1 = round(stat.mean(flat_blue1), 4)
    D_BLUE1 = round(stat.variance(flat_blue1), 4)

    MO_BRIGHT1 = round(stat.mean(flat_gray1), 4)
    D_BRIGHT1 = round(stat.variance(flat_gray1), 4)

    MO_RED2 = round(stat.mean(flat_red2), 4)
    D_RED2 = round(stat.variance(flat_red2), 4)

    MO_GREEN2 = round(stat.mean(flat_green2), 4)
    D_GREEN2 = round(stat.variance(flat_green2), 4)

    MO_BLUE2 = round(stat.mean(flat_blue2), 4)
    D_BLUE2 = round(stat.variance(flat_blue2), 4)

    MO_BRIGHT2 = round(stat.mean(flat_gray2), 4)
    D_BRIGHT2 = round(stat.variance(flat_gray2), 4)

    print('Мат ожидание красного спектра первого изображения = ', MO_RED1)
    print('Дисперсия красного спектра первого изображения = ', D_RED1)

    print('Мат ожидание зеленого спектра первого изображения = ', MO_GREEN1)
    print('Дисперсия красного спектра первого изображения = ', D_GREEN1)

    print('Мат ожидание синего спектра первого изображения = ', MO_BLUE1)
    print('Дисперсия синего спектра первого изображения = ', D_BLUE1)

    print('Мат ожидание яркости первого изображения = ', MO_BRIGHT1)
    print('Дисперсия яркости первого изображения = ', D_BRIGHT1)

    print('Мат ожидание красного спектра второго изображения = ', MO_RED2)
    print('Дисперсия красного спектра второго изображения = ', D_RED2)

    print('Мат ожидание зеленого спектра второго изображения = ', MO_GREEN2)
    print('Дисперсия красного спектра второго изображения = ', D_GREEN2)

    print('Мат ожидание синего спектра второго изображения = ', MO_BLUE2)
    print('Дисперсия красного спектра второго изображения = ', D_BLUE2)

    print('Мат ожидание яркости второго изображения = ', MO_BRIGHT2)
    print('Дисперсия яркости второго изображения = ', D_BRIGHT2)

    print('Ковариационная матрица красного спектра 2 изображений')
    string_red = 'Ковариационная матрица\n'

    COV_MATRIX_RED = np.cov([flat_red1, flat_red2])
    for string in range(COV_MATRIX_RED.__len__()):
        for item in range(COV_MATRIX_RED[string].__len__()):
            string_red += "{0:.4f}".format(COV_MATRIX_RED[string][item]) + '    '
            print("{0:.4f}".format(COV_MATRIX_RED[string][item]), end='    ')
        print()
        string_red += '\n'

    print('Ковариационная матрица зеленого спектра 2 изображений')
    string_green = 'Ковариационная матрица\n'
    COV_MATRIX_GREEN = np.cov([flat_green1, flat_green2])
    for string in range(COV_MATRIX_GREEN.__len__()):
        for item in range(COV_MATRIX_GREEN[string].__len__()):
            string_green += "{0:.4f}".format(COV_MATRIX_GREEN[string][item]) + '    '
            print("{0:.4f}".format(COV_MATRIX_GREEN[string][item]), end='    ')
        print()
        string_green += '\n'

    print('Ковариационная матрица синего спектра 2 изображений')
    string_blue = 'Ковариационная матрица\n'
    COV_MATRIX_BLUE = np.cov([flat_blue1, flat_blue2])
    for string in range(COV_MATRIX_BLUE.__len__()):
        for item in range(COV_MATRIX_BLUE[string].__len__()):
            string_blue += "{0:.4f}".format(COV_MATRIX_BLUE[string][item]) + '  '
            print("{0:.4f}".format(COV_MATRIX_BLUE[string][item]), end='    ')
        print()
        string_blue += '\n'

    print('Ковариационная матрица')
    COV_MATRIX_BRIGHT = np.cov([flat_gray1, flat_gray2])
    string_bright = 'Ковариационная матрица спектра яркости 2 изображений\n'
    for string in range(COV_MATRIX_BRIGHT.__len__()):
        for item in range(COV_MATRIX_BRIGHT[string].__len__()):
            string_bright += "{0:.4f}".format(COV_MATRIX_BRIGHT[string][item]) + '  '
            print("{0:.4f}".format(COV_MATRIX_BRIGHT[string][item]), end='    ')
        print()
        string_bright += '\n'

    data_red = "МО_1 = " + str(MO_RED1) + '\n' + 'Д_1 = ' + str(D_RED1) + "\nМО_2 = " + str(MO_RED2) + '\n' +\
               'Д_2 = ' + str(D_RED2) + '\n' + string_red
    data_green = "МО_1 = " + str(MO_GREEN1) + '\n' + 'Д_1 = ' + str(D_GREEN1) + "\nМО_2 = " + str(MO_GREEN2) + '\n' + \
                 'Д_2 = ' + str(D_GREEN2) + '\n' + string_green
    data_blue = "МО_1 = " + str(MO_BLUE1) + '\n' + 'Д_1 = ' + str(D_BLUE1) + "\nМО_2 = " + str(MO_BLUE2) + '\n' + \
                'Д_2 = ' + str(D_BLUE2) + '\n' + string_blue
    data_bright = "МО_1 = " + str(MO_BRIGHT1) + '\n' + 'Д_1 = ' + str(D_BRIGHT1) + "\nМО_2 = " + str(MO_BRIGHT2) + \
                  '\n' + 'Д_2 = ' + str(D_BRIGHT2) + '\n' + string_bright

    spectr_razlozh_for_two(flat_red1, flat_red2, 'Красный спектр', data_red)
    spectr_razlozh_for_two(flat_green1, flat_green2, 'Зеленый спектр', data_green)
    spectr_razlozh_for_two(flat_blue1, flat_blue2, 'Синий спектр', data_blue)
    spectr_razlozh_for_two(flat_gray1, flat_gray2, 'Спектр яркости', data_bright)


def load_image():
    """
    Считывает путь до файла, проверяет создан ли он, является ли файлом и имеет
    расширение .jpg
    :return: возвращает объекти типа image в случае успеха и пустой False иначе
    """
    testpath = input('Введите адрес: ')
    if os.path.exists(testpath):
        if os.path.isfile(testpath):
            if testpath.endswith(('.JPG', '.jpg', '.jpeg')):
                return imread(testpath)
            else:
                print("файл должен иметь расширение .jpg")
        else:
            print("Это не файл")
    else:
        print("Данного пути не существует")
    return False


def one_image():
    img = load_image()
    if img:
        analyz(img)
    else:
        print("Ошибка")


def one_cut_image():
    img = load_image()
    if img:
        analyz(cut_image(img))
    else:
        print("Ошибка")


def two_image():
    img1 = load_image()
    img2 = load_image()
    if not(isinstance(img1, bool) or isinstance(img2, bool)):
        sravn_analyz(img1, img2)
    else:
        print("Ошибка")


def otvet():
    print('Такой функции нет.')


if __name__ == '__main__':
    COMMAND = {'1': one_image, '2': one_cut_image, '3': two_image}
    answer = input('1.Обработка одного изображения\n'
                   '2.Обработка выделенной области изображения\n'
                   '3.Совместная обработка 2 изображений\n')
    client_handler = COMMAND.get(answer, otvet)
    client_handler()
