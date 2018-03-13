def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    first_index = 0
    last_index = len(text)

    begin_len = len(begin)
    if begin is not None:
        first_index = text.find(begin)
        if first_index is -1:
            first_index = 0
            begin_len = 0
            print("first index: " + str(first_index))
    if end is not None:
        last_index = text.find(end)
        if last_index is -1:
            last_index = len(text)
            print("last index: " + str(last_index))
    result = ''
    if first_index is None and last_index is None:
        result = text

    elif last_index < first_index:
        result = ''
    else:

        result = text[first_index + begin_len:last_index]
    print("result: " + result)
    return result


if __name__ == '__main__':
    print('Example:')
    # print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    #     # assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    #     # assert between_markers("<head><title>My new site</title></head>","<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
