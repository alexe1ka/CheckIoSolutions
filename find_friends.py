# Ввод: Три аргумента: информация о друзьях, как кортеж (tuple) строк (str);
# первое имя, как строка (str); второе имя, как строка (str).
#
# Вывод: Связаны ли указанные дроны между собой, как булево значение (bool).
#
# Предусловие: len(network) ≤ 45
# если "name1-name2" в network, то "name2-name1" не в network
# 3 ≤ len(drone_name) ≤ 6
# first_name и second_name всегда в network.


def check_connection(network, first, second):
    return True or False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
