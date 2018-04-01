# Даны длины сторон треугольника и необходимо найти углы треугольника.
# Если невозможно сформировать треугольник из данных сторон (или для вырожденного треугольника),
# тогда результатом должны быть все нули. Результат должен быть представлен,
# как список (list) целых чисел в возрастающем порядке.
# Углы должны быть записаны в градусах и округляются до целого числа (стандартное округление).
#
# Входные данные: Длины сторон треугольник, как целые числа (int).
#
# Выходные данные: Углы данного треугольника в градусах, как сортированный список (list) целых чисел (int).
#
# Предусловия:
# 0 < a,b,c ≤ 1000
import math


def checkio(a, b, c):
    # replace this for solution
    if is_triangle(a, b, c):
        angle_alp = calc_angle(a, b, c)
        angle_bet = calc_angle(a, c, b)
        angle_gam = 180 - angle_alp - angle_bet
        # print("angle a = {}, angle b = {}, angle_c = {}".format(angle_a, angle_b, 180 - angle_a - angle_b))
        return sorted([angle_alp, angle_bet, angle_gam])
    else:
        return [0, 0, 0]


def is_triangle(a, b, c) -> bool:
    len_list = sorted([a, b, c])
    return True if len_list[2] < len_list[1] + len_list[0] else False


def calc_angle(side_a, side_b, side_c):
    return round(math.degrees(math.acos((pow(side_a, 2) + pow(side_c, 2) - pow(side_b, 2)) / (2 * side_a * side_c))))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(4, 4, 4))
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
