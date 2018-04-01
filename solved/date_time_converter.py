# Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
# Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
# Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.

import datetime


def date_time(time):
    # replace this for solution
    current_date = time.split(" ")[0].split(".")
    current_time = time.split(" ")[1].split(":")
    data_obj = datetime.datetime(int(current_date[2]), int(current_date[1]), int(current_date[0]),
                                 int(current_time[0]), int(current_time[1]))

    print("current hour = {}, current minute = {}".format(current_time[0].lstrip("0").replace(" 0", " "),
                                                          current_time[1].lstrip("0").replace(" 0", " ")))
    return data_obj.strftime("%d %B %Y year %H {} %M {}").lstrip("0").replace(" 0", " ").format(
        "hour" if current_time[0].lstrip("0").replace(" 0", " ") == "1" else "hours", "minute" if current_time[0].lstrip("0").replace(" 0", " ") == "1" else "minutes")


if __name__ == '__main__':
    # print("Example:")
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print(date_time("11.04.1812 01:01"))
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    # assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    # assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
