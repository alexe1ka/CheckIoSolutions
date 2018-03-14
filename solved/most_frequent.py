def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    result_dict = dict.fromkeys(set(data))
    for string in set(data):
        result_dict[string] = count_current_element_in_list(data, string)
    return max(result_dict.keys(), key=(lambda k: result_dict[k]))


def count_current_element_in_list(data_list: list, current_element: str) -> int:
    len_start_list = len(data_list)
    while current_element in data_list:
        data_list.remove(current_element)
    return len_start_list - len(data_list)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ])

    # assert most_frequent([
    #     'a', 'b', 'c',
    #     'a', 'b',
    #     'a'
    # ]) == 'a'
    #
    # assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
