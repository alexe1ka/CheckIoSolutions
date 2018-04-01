# необходимо найти самую частую букву в тексте.
# Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения,
# так что при подсчете считайте, что "A" == "a".
# Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
#
# Если в тексте две и больше буквы с одинаковой частотой,
# тогда результатом будет буква, которая идет первой в алфавите.
# Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
#
# Вх. данные: Текст для анализа, как строка.
# Вых. данные: Наиболее частая буква, как строка.
#
# Предусловия:
# text содержит только ASCII символы.
# 0 < len(text) ≤ 105
import re


def checkio(text):
    # replace this for solution
    clean_lst_with_letters = list(filter(None, [re.sub(r'[^A-Za-z]+', '', x) for x in sorted(text.lower())]))
    res_let = ""
    max_let_cnt = 0
    for let in sorted(set(clean_lst_with_letters)):
        count = clean_lst_with_letters.count(let)
        if count > max_let_cnt:
            max_let_cnt = count
            res_let = let
    return res_let


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio("Hello World!") == "l", "Hello test"
    # assert checkio("How do you do?") == "o", "O is most wanted"

    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
