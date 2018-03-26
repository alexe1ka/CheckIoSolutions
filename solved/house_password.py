# Пароль считается достаточно стойким, если его длина
# больше или равна 10 символам, он содержит, как
# минимум одну цифру, одну букву в верхнем и одну в
# нижнем регистре.Пароль может содержать только
# латинские буквы и / или цифры.

import re


def checkio(data):
    # replace this for solution
    return len(data) >= 10 and bool(re.search("\d", data)) and bool(re.search("\d", data)) and bool(
        re.search("[A-Z]", data)) and bool(re.search("[a-z]", data))


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print(checkio('A1213pokl'))
    # print(checkio('bAse730onE4'))

    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
