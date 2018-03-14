OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if str(operation) == "conjunction":
        return (x and y).__int__()
    elif str(operation) == "disjunction":
        return (x or y).__int__()
    elif str(operation) == "implication":
        if x > y:
            return y.__int__()
        elif x == y:
            return 1
        else:
            return 1
    elif str(operation) == "exclusive":
        return (x != y).__int__()
    elif str(operation) == "equivalence":
        return (x == y).__int__()
    else:
        return -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert boolean(1, 0, "conjunction") == 0, "and"
    print(boolean(1, 0, "conjunction"))
    assert boolean(1, 0, "disjunction") == 1, "or"
    print(boolean(1, 0, "disjunction"))
    assert boolean(1, 1, "implication") == 1, "material"
    print(boolean(1, 1, "implication"))
    assert boolean(0, 1, "exclusive") == 1, "xor"
    print(boolean(0, 1, "exclusive"))
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print(boolean(0, 1, "equivalence"))
