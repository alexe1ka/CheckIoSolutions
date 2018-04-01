# список замкнутых интервалов


def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    data = sorted(data)
    res = []
    while data:
        interval = make_interval(data)
        res.append(interval)
        data = data[data.index(interval[1]) + 1:]
    print(res)
    return res


def make_interval(data):
    if len(data) == 1:
        return data[0], data[0]
    start_num = data[0]
    prev_num = data[0] - 1
    for num in data:
        if num - prev_num == 1:
            prev_num = num
    return start_num, prev_num


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))
    print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}))
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    # print('Almost done! The only thing left to do is to Check it!')
