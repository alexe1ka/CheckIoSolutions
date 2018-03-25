# Дан текст с разными словами и/или числами, которые разделены пробелами и знаками пунктуации.
# Числа не считаются за слова (также как и смесь букв и цифр). Необходимо подсчитать слова,
# в которых гласные буквы чередуются с согласными (полосатые слова),
# то есть в таких словах нет двух гласных или двух согласных букв подряд.
# Слова состоящие из одной буквы - не "полосатые" (не считайте их). Регистр букв не имеет значения.
#
# Входные данные: Текст, как строка (str).
#
# Выходные данные: Количество "полосатых" слов, как целое число (int).
#
# Предусловия:Текст содержит только ASCII символы.
# 0 < len(text) < 105


VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
