def human_years_cat_years_dog_years(human_years: int) -> list:
    """
    Перевод человеческих лет в кошачки и собачьи года.

    :param human_years: человеческие годы, принимает значение human_years >= 1
    :return: список из человеческих, кошачьих и собачьих лет
    """

    # 15 лет за первый человеческий год.
    cat_years = 15
    dog_years = 15

    year = 1  # Первый год.

    while year <= human_years:
        if year == 2:
            cat_years += 9
            dog_years += 9
        elif year > 2:
            cat_years += 4
            dog_years += 5
        year += 1

    return [human_years, cat_years, dog_years]


assert human_years_cat_years_dog_years(1) == [1, 15, 15]
assert human_years_cat_years_dog_years(2) == [2, 24, 24]
assert human_years_cat_years_dog_years(10) == [10, 56, 64]
