# Вам предлагается некоторый текст, который может содержать осмысленные слова.
# Вы должны подсчитать количество таких слов в этом тексте. Слово может стоять отдельно,
# а может присутствовать как часть другого слова. Регистр букв не имеет значения.
# Слова даны в нижнем регистре и не повторяются. Если слово встречается в тексте несколько раз,
# оно должно быть посчитано только один раз.
#
# Например, текст "How aresjfhdskfhskd you?", слова - ("how", "are", "you", "hello"). Результат должен быть равен 3.
#
# Вход: Два аргумента. Текст как строка (юникод в Python 2) и слова в виде множества (set) строк (юникод в Python 2).
#
# Выход: Количество слов в тексте в виде целого числа.

import re


def count_words(text, words):
    words = list(words)
    count = 0
    for i in range(len(words)):
        if text.lower().__contains__(words[i].lower()):
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
