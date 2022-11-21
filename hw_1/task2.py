FACING = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
ROTATION_DEGREE = 45  # Градус поворота.


def new_direction(facing: str, turn: int) -> str:
    """
    Определяет, в каком направлении вы окажаетесь после поворота на заданный градус
    от заданной стороны света.

    :param facing: сторона света
    :param turn: градус поворота, кратен 45 и находится в диапазоне между -1080 и 1080
    :return: сторона света
    """

    index_of_facing = FACING.index(facing)  # Индекс заданной стороны света.

    if all([turn % 45 == 0, -1080 <= turn <= 1080]):

        number_of_turns = turn // 45  # Количество поворотов, которое нужно сделать.

        idx_of_new_direction = index_of_facing + number_of_turns  # Индекс стороны света, после поворота.

        # Проверяем, входит ли новый индекс в индексы заданного списка FACING (от 0 до 7).
        if 0 <= idx_of_new_direction <= len(FACING) - 1:
            return FACING[idx_of_new_direction]
        else:
            idx = idx_of_new_direction % len(FACING)
            return FACING[idx]
    else:
        print("Необходимо передать в функцию параметр turn, удовлетворяющий условиям:\n"
              "turn % 45 == 0 и -1080 <= turn <= 1080")


assert new_direction("S", 180)
assert new_direction("SE", -45)
assert new_direction("W", 495)
