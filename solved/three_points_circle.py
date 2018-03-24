import math


def checkio(data):
    # replace this for solution
    lst_data = eval("(%s)" % data)

    if lst_data[0][0] == lst_data[1][0] or lst_data[1][0] == lst_data[2][0]:
        lst_data = sorted(lst_data, key=lambda point: point[1])

    print("lst_data: {}".format(lst_data))

    m_a = k_calculate(lst_data[0], lst_data[1])
    m_b = k_calculate(lst_data[1], lst_data[2])
    x = calc_x(m_a, m_b, lst_data[0], lst_data[1], lst_data[2])
    y = calc_y(lst_data[0], lst_data[1], lst_data[2], x)

    r = (radius_calc([x, y], lst_data[0]))
    return "(x-{})^2+(y-{})^2={}^2" \
        .format(round(x, 2) if not round(x, 2).is_integer() else round(x.__int__()),
                round(y, 2) if not round(y, 2).is_integer() else round(y.__int__()),
                round(r, 2) if not round(r, 2).is_integer() else round(r.__int__()))


def calc_x(m_a, m_b, point1, point2, point3):
    # print("m_a = {}, m_ba = {}".format(m_a, m_b))
    try:
        return (((m_a * m_b) * (point1[1] - point3[1]))
                + (m_b * (point1[0] + point2[0]))
                - (m_a * (point2[0] + point3[0]))) \
               / (2 * (m_b - m_a))
    except ZeroDivisionError:
        return 0


def calc_y(point1: list, point2: list, point3: list, x: int) -> float:
    try:
        return (-(1 / k_calculate(point1, point2))
                * (x - ((point1[0] + point2[0]) / 2))) \
               + ((point1[1] + point2[1]) / 2)
    except ZeroDivisionError:
        return (-(1 / k_calculate(point2, point3))
                * (x - ((point2[0] + point3[0]) / 2))) \
               + ((point2[1] + point3[1]) / 2)


def k_calculate(point1: list, point2: list) -> int:
    # print("k_calc: point1: {} , point2: {}".format(point1, point2))
    try:
        return (point2[1] - point1[1]) / (point2[0] - point1[0])
    except ZeroDivisionError:
        return 0


def radius_calc(center: list, point: list) -> float:
    return round(math.sqrt(math.pow(point[1] - center[1], 2) + math.pow(point[0] - center[0], 2)), 2)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print(checkio("(2,2),(6,2),(2,6)"))

    print(checkio("(2,2),(6,2),(2,6)"))
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"

    print(checkio("(3,7),(6,9),(9,7)"))
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

    print(checkio("(7,7),(4,3),(1,8)"))
    assert checkio("(7,7),(4,3),(1,8)") == "(x-3.8)^2+(y-6.28)^2=3.28^2"

    print(checkio("(7,3),(9,6),(3,6)"))
    assert checkio("(7,3),(9,6),(3,6)") == "(x-6)^2+(y-5.83)^2=3^2"

    print(checkio("(9,8),(9,4),(3,6)"))
    assert checkio("(9,8),(9,4),(3,6)") == "(x-6.33)^2+(y-6)^2=3.33^2"
