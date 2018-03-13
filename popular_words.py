def popular_words(text, words) -> dict:
    # your code here
    result_dict = dict.fromkeys(words)
    print(result_dict)
    for word in words:
        print(word_in_current_text_calculator(text, word))
        print("result dict: " + result_dict)
    return None


def word_in_current_text_calculator(text: str, word: str) -> int:
    return text.lower().count(word.lower())


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing

#     assert popular_words('''
# When I was One,
# I had just begun.
# When I was Two,
# I was nearly new.
# ''', ['i', 'was', 'three']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")
