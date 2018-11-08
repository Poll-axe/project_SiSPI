import matplotlib
import numpy


def spectr(a):
    """

    :param a:
    """
    matplotlib.pyplot.hist(a, 100)
    matplotlib.pyplot.show()


def mat(a):
    """

    :param a:
    :return:
    """
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return float(sum / len(a))


def disp(a):
    """

    :param a:
    :return:
    """
    Mat_a = mat(a)
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - Mat_a) ** 2
    return float(sum / (len(a) - 1))


def cov(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - mat(a)) * (b[i] - mat(b))
    return float(sum / (len(a) - 1))


def calculation(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    """
    Mat_a = mat(a)
    Mat_b = mat(b)
    Mat_c = mat(c)
    Disp_a = disp(a)
    Disp_b = disp(b)
    Disp_c = disp(c)


if __name__ == '__main__':
    a = numpy.random.randn(1000)
    b = numpy.random.randn(1000)
    print(mat(a))
    print(disp(a))
    print(cov(a, b))
    spectr(a)
