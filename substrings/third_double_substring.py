def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    # your code here
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')

# Вы должны найти подстроку,
# которая повторяется больше одного раза в данной строке и при этом повторения друг на друга не накладываются.
# Например, в строке "abcab" самая длинная подстрока,
# которая повторяется более одного раза, это "ab",
# поэтому ответом должно быть число 2 (длина "ab").
