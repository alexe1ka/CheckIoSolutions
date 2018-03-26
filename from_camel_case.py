def from_camel_case(name):
    # replace this for solution
    # конвертнуть camelCaseNotation в not_camel_case_notation
    res = ""
    for ch in name:
        if ch.isupper():
            if name.index(ch) != 0:
                res += "_" + ch.lower()
            else:
                res += ch.lower()
        else:
            res += ch
    return res


if __name__ == '__main__':
    print("Example:")
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
