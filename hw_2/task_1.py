# TODO: реализовать ф-ию enumerate с помощью zip

from itertools import count


def enumerate_with_zip(iterable_obj, start=0):
    """
    Реализация функции enumerate с помощью zip.
    :param iterable_obj: любая последовательность
    :param start: число, с которого начинается нумерация элементов последовательности, по умолчанию 0
    :return: zip object
    """

    return zip(count(start, 1), iterable_obj)


if __name__ == "__main__":

    list_ = ["Harry", "Potter", "Ron", "Weasley", "Hermione", "Grander"]

    for number, item in enumerate_with_zip(list_, 1):
        print(number, item)
