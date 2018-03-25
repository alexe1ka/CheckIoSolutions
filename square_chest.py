# Панель представляет собой решетку из пронумерованных точек.
# Решетка состоит из прямоугольной матрицы точек и линий,
# соединяющих некоторые пары близлежащих точек. Решением является код, равный количеству квадратов,
# образованных линиями. Например, на фигуре, представленной ниже, есть три квадрата: два малых и один средний.
#
# Точки пронумерованы от 1 до 16. Линии представлены как списки (list) из двух чисел (концы линий).
#
# Входные данные: Описания линий в виде списка (list) списков (list), каждый из которых содержит два целых числа.
#
# Выходные данные: Количество квадратов в виде целого числа.
#
# Предусловия:
# 0 < len(lines) ≤ 32


def checkio(lines_list):
    """Return the quantity of squares"""
    return 0


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
