# Анаграммы - это игра со словами, в которой переставляя в словах или фразах буквы местами,
# мы получаем новые слова или фразы. Два слова анаграммы друг для друга,
# если одно можно получить из другого перестановкой букв. Также для анаграмм регистр букв и пробелы не имеют значения.
# Для примера, "Gram Ring Mop" и "Programming" -- анаграммы. Но вот "Hello" и "Ole Oh" уже нет.
#
# Итак, вам даны два слова или фразы. Попробуйте определить анаграммы ли они друг для друга.
#
# Входные данные: Два аргумента, как строки (str, unicode).
#
# Выходные данные: Анаграммы это или нет, как булево значение (True или False)
#
# Предусловия: 0 < |first_word| < 100;
# 0 < |second_word| < 100;
# Слова состоят только латинских ASCII букв и пробелов.
import re


def verify_anagrams(first_word, second_word):
    return True if make_clean_list_with_letters(first_word) == make_clean_list_with_letters(second_word) else False


def make_clean_list_with_letters(word):
    return sorted(list(filter(None, [re.sub(r'[^A-Za-z]+', '', x) for x in sorted(word.lower())])))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(verify_anagrams("Kings Lead Hat", "Talking Heads"))

    # assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    # assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    # assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    # assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
