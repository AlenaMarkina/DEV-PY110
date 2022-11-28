# Решила двумя способами.

str_ = "harry( potter(and)ron) with hermione"


def first_version(string: str) -> str:
    """
    Удаляет из строки пару скобок (открывающие и закрывающие), а также все, что находится между скобками.
    Учитываем только внешнюю пару скобок.
    :param string: исходная строка
    :return: форматированная строка
    """

    idx_1 = string.find("(")
    idx_2 = 0

    # Находим индекс закрывающей скобки.
    for i in range(-1, -len(string)-1, -1):
        if string[i] == ")":
            idx_2 = len(string) - (-i)
            break

    return string.replace(string[idx_1:idx_2+1], '')


def second_version(string):
    idx_1 = string.find("(")
    idx_2 = string.rfind(")")
    return string.replace(string[idx_1:idx_2+1], "")


print(first_version(str_))
print(second_version(str_))
