def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here

    print(data)
    for string in data:
        count = len(remove_all_current_elements_from_list(data, string))
        print(count)

    # return None


def remove_all_current_elements_from_list(data_list: list, current_element: str) -> list:
    if len(data_list) is 1:
        return data_list
    while current_element in data_list:
        data_list.remove(current_element)
    return data_list


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
