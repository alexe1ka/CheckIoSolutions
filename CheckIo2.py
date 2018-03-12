import re


def say_hi(name, age):
    return "Hi. My name is " + name + " and I'm " + str(age) + " years old"


#####################################################
def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text


#######################################################
def first_word(text: str) -> str:
    """
        returns the first word in a given text
    """
    word = re.search("[A-Z]*[a-z]*[']*[a-z]", text)
    return word.group(0)


################################################################
def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    second_ind = text.replace(symbol, "", 1).find(symbol) + 1
    if second_ind == 0:
        return
    return second_ind


#####################################################################
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    return ''
