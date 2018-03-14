import datetime


def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    date1 = convert_tuple_to_date(date1)
    date2 = convert_tuple_to_date(date2)
    return abs((date2 - date1).days)


def convert_tuple_to_date(tuple_date: tuple) -> datetime.date:
    return datetime.date(tuple_date[0], tuple_date[1], tuple_date[2])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
