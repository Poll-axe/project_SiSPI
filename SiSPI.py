import os
from time import sleep

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
    name = 'spectr_razlozh' + name_title + '.jpg'
    pyp.savefig(PATH + '\\' + name)
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
    name = 'spectr_razlozh_for_two' + name_title + '.jpg'
    pyp.savefig(PATH + "\\" + name)
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
    img_f = img_as_float(img)
    pyp.subplot(231), pyp.imshow(img, 'gray'), pyp.title('Картинка')

    pyp.tick_params(axis='both', labelleft=False,
                    labelright=False, labelbottom=False)
    pyp.show()

    # получение каналов изображения
    red = img_f[:, :, 0]
    green = img_f[:, :, 1]
    blue = img_f[:, :, 2]

    # перевод канналов в одномерные массивы
    flat_red = red.ravel()
    flat_green = green.ravel()
    flat_blue = blue.ravel()

    # получение яркости изображения
    truegray = skimage.color.rgb2grey(img_f)
    flat_gray = truegray.ravel()
    mo_red = round(stat.mean(flat_red), 4)
    d_red = round(stat.variance(flat_red), 4)

    mo_green = round(stat.mean(flat_green), 4)
    d_green = round(stat.variance(flat_green), 4)

    mo_blue = round(stat.mean(flat_blue), 4)
    d_blue = round(stat.variance(flat_blue), 4)

    print('Мат ожидание красного спектра = ', mo_red)
    print('Дисперсия красного спектра = ', d_red)

    print('Мат ожидание зеленого спектра = ', mo_green)
    print('Дисперсия красного спектра = ', d_green)

    print('Мат ожидание синего спектра = ', mo_blue)
    print('Дисперсия синего спектра = ', d_blue)
    print('Cov matrix')
    data_cov = '\nМатрица ковариации каналов \n'
    cov_matrix = np.cov([flat_red, flat_green, flat_blue])
    for string in range(cov_matrix.__len__()):
        for item in range(cov_matrix[string].__len__()):
            cov_matrix[string][item].__round__(4)
            data_cov += "{0:.4f}".format(cov_matrix[string][item]) + '   '
            print("{0:.4f}".format(cov_matrix[string][item]), end='    ')
        print()
        data_cov += '\n'

    data_red = "МО = " + str(mo_red) + '\n' + 'Д = ' + str(d_red)
    data_green = "МО = " + str(mo_green) + '\n' + 'Д = ' + str(d_green)
    data_blue = "МО = " + str(mo_blue) + '\n' + 'Д = ' + str(d_blue)
    spectr_razlozh(flat_red, 'Красный спектр', data_red)
    spectr_razlozh(flat_green, 'Зеленый спектр', data_green)
    spectr_razlozh(flat_blue, 'Синий спектр', data_blue)

    mo_bright = round(stat.mean(flat_gray), 4)
    d_bright = round(stat.variance(flat_gray), 4)
    print('Мат ожидание яркости = ', mo_bright)
    print('Дисперсия яркости = ', d_bright)
    data_bright = "МО = " + str(mo_bright) + '\n' + 'Д = ' + str(d_bright) + data_cov
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
    pyp.show()

    # получение каналов изображения
    red1 = imgf1[:, :, 0]
    green1 = imgf1[:, :, 1]
    blue1 = imgf1[:, :, 2]

    # перевод канналов в одномерные массивы
    flat_red1 = red1.ravel()
    flat_green1 = green1.ravel()
    flat_blue1 = blue1.ravel()
    true_gray1 = skimage.color.rgb2grey(imgf1)
    flat_gray1 = true_gray1.ravel()

    img_f2 = img_as_float(img2)
    pyp.subplot(231), pyp.imshow(img2, 'gray'), pyp.title('Kартинка 2')

    pyp.tick_params(axis='both', labelleft=False,
                    labelright=False, labelbottom=False)
    pyp.show()

    # получение каналов изображения
    red2 = img_f2[:, :, 0]
    green2 = img_f2[:, :, 1]
    blue2 = img_f2[:, :, 2]

    # перевод канналов в одномерные массивы
    flat_red2 = red2.ravel()
    flat_green2 = green2.ravel()
    flat_blue2 = blue2.ravel()
    truegray2 = skimage.color.rgb2grey(img_f2)
    flat_gray2 = truegray2.ravel()

    # Вычисление данных
    mo_red1 = round(stat.mean(flat_red1), 4)
    d_red1 = round(stat.variance(flat_red1), 4)

    mo_green1 = round(stat.mean(flat_green1), 4)
    d_green1 = round(stat.variance(flat_green1), 4)

    mo_blue1 = round(stat.mean(flat_blue1), 4)
    d_blue1 = round(stat.variance(flat_blue1), 4)

    mo_bright1 = round(stat.mean(flat_gray1), 4)
    d_bright1 = round(stat.variance(flat_gray1), 4)

    mo_red2 = round(stat.mean(flat_red2), 4)
    d_red2 = round(stat.variance(flat_red2), 4)

    mo_green2 = round(stat.mean(flat_green2), 4)
    d_green2 = round(stat.variance(flat_green2), 4)

    mo_blue2 = round(stat.mean(flat_blue2), 4)
    d_blue2 = round(stat.variance(flat_blue2), 4)

    mo_bright2 = round(stat.mean(flat_gray2), 4)
    d_bright2 = round(stat.variance(flat_gray2), 4)

    print('Мат ожидание красного спектра первого изображения = ', mo_red1)
    print('Дисперсия красного спектра первого изображения = ', d_red1)

    print('Мат ожидание зеленого спектра первого изображения = ', mo_green1)
    print('Дисперсия красного спектра первого изображения = ', d_green1)

    print('Мат ожидание синего спектра первого изображения = ', mo_blue1)
    print('Дисперсия синего спектра первого изображения = ', d_blue1)

    print('Мат ожидание яркости первого изображения = ', mo_bright1)
    print('Дисперсия яркости первого изображения = ', d_bright1)

    print('Мат ожидание красного спектра второго изображения = ', mo_red2)
    print('Дисперсия красного спектра второго изображения = ', d_red2)

    print('Мат ожидание зеленого спектра второго изображения = ', mo_green2)
    print('Дисперсия красного спектра второго изображения = ', d_green2)

    print('Мат ожидание синего спектра второго изображения = ', mo_blue2)
    print('Дисперсия красного спектра второго изображения = ', d_blue2)

    print('Мат ожидание яркости второго изображения = ', mo_bright2)
    print('Дисперсия яркости второго изображения = ', d_bright2)

    print('Ковариационная матрица красного спектра 2 изображений')
    string_red = 'Ковариационная матрица\n'

    cov_matrix_red = np.cov([flat_red1, flat_red2])
    for string in range(cov_matrix_red.__len__()):
        for item in range(cov_matrix_red[string].__len__()):
            string_red += "{0:.4f}".format(cov_matrix_red[string][item]) + '    '
            print("{0:.4f}".format(cov_matrix_red[string][item]), end='    ')
        print()
        string_red += '\n'

    print('Ковариационная матрица зеленого спектра 2 изображений')
    string_green = 'Ковариационная матрица\n'
    cov_matrix_green = np.cov([flat_green1, flat_green2])
    for string in range(cov_matrix_green.__len__()):
        for item in range(cov_matrix_green[string].__len__()):
            string_green += "{0:.4f}".format(cov_matrix_green[string][item]) + '    '
            print("{0:.4f}".format(cov_matrix_green[string][item]), end='    ')
        print()
        string_green += '\n'

    print('Ковариационная матрица синего спектра 2 изображений')
    string_blue = 'Ковариационная матрица\n'
    cov_matrix_blue = np.cov([flat_blue1, flat_blue2])
    for string in range(cov_matrix_blue.__len__()):
        for item in range(cov_matrix_blue[string].__len__()):
            string_blue += "{0:.4f}".format(cov_matrix_blue[string][item]) + '  '
            print("{0:.4f}".format(cov_matrix_blue[string][item]), end='    ')
        print()
        string_blue += '\n'

    print('Ковариационная матрица')
    cov_matrix_bright = np.cov([flat_gray1, flat_gray2])
    string_bright = 'Ковариационная матрица спектра яркости 2 изображений\n'
    for string in range(cov_matrix_bright.__len__()):
        for item in range(cov_matrix_bright[string].__len__()):
            string_bright += "{0:.4f}".format(cov_matrix_bright[string][item]) + '  '
            print("{0:.4f}".format(cov_matrix_bright[string][item]), end='    ')
        print()
        string_bright += '\n'

    data_red = "МО_1 = " + str(mo_red1) + '\n' + 'Д_1 = ' + str(d_red1) + "\nМО_2 = " + str(mo_red2) + '\n' + \
               'Д_2 = ' + str(d_red2) + '\n' + string_red
    data_green = "МО_1 = " + str(mo_green1) + '\n' + 'Д_1 = ' + str(d_green1) + "\nМО_2 = " + str(mo_green2) + '\n' + \
                 'Д_2 = ' + str(d_green2) + '\n' + string_green
    data_blue = "МО_1 = " + str(mo_blue1) + '\n' + 'Д_1 = ' + str(d_blue1) + "\nМО_2 = " + str(mo_blue2) + '\n' + \
                'Д_2 = ' + str(d_blue2) + '\n' + string_blue
    data_bright = "МО_1 = " + str(mo_bright1) + '\n' + 'Д_1 = ' + str(d_bright1) + "\nМО_2 = " + str(mo_bright2) + \
                  '\n' + 'Д_2 = ' + str(d_bright2) + '\n' + string_bright

    spectr_razlozh_for_two(flat_red1, flat_red2, 'Красный спектр', data_red)
    spectr_razlozh_for_two(flat_green1, flat_green2, 'Зеленый спектр', data_green)
    spectr_razlozh_for_two(flat_blue1, flat_blue2, 'Синий спектр', data_blue)
    spectr_razlozh_for_two(flat_gray1, flat_gray2, 'Спектр яркости', data_bright)


def save_path():
    while True:
        global PATH
        print("Путь по умолчанию: C:\\Users\\Public\\Pictures")
        print("Введите end что бы прекратить ввод или Enter что бы выбрать путь по умолчанию\n или")
        path_new = input('Введите путь до папки, где сохранить результаты работы программы: ')
        if path_new == 'end':
            print("Выход из меню ввода")
            sleep(2)
            print("Завершение работы программы")
            break
        print(path_new)
        if path_new == '':
            if os.path.exists(PATH):
                if os.path.isdir(PATH):
                    print("Выбран путь по умолчанию")
                    return True
            else:
                print("К сожалению путь по умолчанию не поддерживается на вашем компьютере, введите сами")

        if os.path.exists(path_new):
            if os.path.isdir(path_new):
                    PATH = path_new
                    return True
            else:
                print("Это не папка")
        else:
            print("Данного пути не существует, попробуйте ещё раз или введте end для того чтобы закончить")

    return False


def load_image():
    """
    Считывает путь до файла, проверяет создан ли он, является ли файлом и имеет
    расширение .jpg
    :return: возвращает объекти типа image в случае успеха и пустой False иначе
    """
    while True:
        test_path = input('Введите путь до изображения: ')

        if test_path == 'end':
            print("Выход из меню ввода")
            sleep(2)
            print("Завершение работы программы")
            break

        if os.path.exists(test_path):
            if os.path.isfile(test_path):
                if test_path.endswith(('.JPG', '.jpg', '.jpeg')):
                    return imread(test_path)
                else:
                    print("файл должен иметь расширение .jpg")
            else:
                print("Это не файл")
        else:
            print("Данного пути не существует, попробуйте ещё раз или введте end для того чтобы закончить")

    return False


def one_image():
    img = load_image()
    if not (isinstance(img, bool)):
        analyz(img)
    else:
        print("Ошибка при открытии файла")


def one_cut_image():
    img = load_image()
    if not (isinstance(img, bool)):
        analyz(cut_image(img))
    else:
        print("Ошибка при открытии файла")


def two_image():
    img1 = load_image()
    img2 = load_image()
    if not (isinstance(img1, bool) or isinstance(img2, bool)):
        sravn_analyz(img1, img2)
    else:
        print("Ошибка при открытии файла")


def otvet():
    print('Такой функции нет.')


# путь для сохранения файлов
PATH = "C:\\Users\\Public\\Pictures"
if __name__ == '__main__':
    if save_path():
        COMMAND = {'1': one_image, '2': one_cut_image, '3': two_image}
        answer = input('1.Обработка одного изображения\n'
                       '2.Обработка выделенной области изображения\n'
                       '3.Совместная обработка 2 изображений\n')
        print("Пожалуйста ожидайте, как только вычисления закончатся мы сообщим вам об этом")
        client_handler = COMMAND.get(answer, otvet)
        client_handler()
    print("Готово")
