import re


def fizz_buzz(number):
    if ((number % 5 == 0) and (number % 3 == 0)):
        return "Fizz Buzz"
    elif (number % 5 == 0):
        return "Buzz"
    elif (number % 3 == 0):
        return "Fizz"
    else:
        print(number)
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.
    # replace this for solution
    return str(number)


############################
def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if (n > len(array) - 1):
        return -1
    else:
        return array[n] ** n
    return None


##########################
def evenTheLast(array):
    if (len(array) != 0):
        evenArr = []
        evenArr = array[::2]
        evenSum = sum(evenArr)
        result = evenSum * array[len(array) - 1]
        return result
    else:
        return 0


#################################
def find_message(text):
    s = ''
    s = re.sub('[^A-Z]', '', text)
    return None


################################
def three_words(words):
    check = (bool)
    count = 0
    for w in words.split():
        if (w.isalpha()):
            count += 1
            if (count == 3):
                return True
        else:
            count = 0
    return False


###############################
def min_max_difference(*args):
    if (len(args) != 0):
        maxim = args[0]
        minim = args[0]
        for n in args:
            if n > maxim:
                maxim = n
            if n < minim:
                minim = n
        if ((float)(maxim - minim).is_integer()):
            return int(maxim - minim)
        else:
            res = format(((float)(maxim - minim)), '.4f')
            return float(res)
    else:
        return 0


##################################################
def left_join(phrases):
    str_phr = ','.join(phrases)
    str_rep = str(str_phr).replace('right', 'left')
    return str_rep


##################################################
def digits_multiplication(number):
    numb_list = [int(x) for x in str(number)]
    print(numb_list)
    result = 1
    for num in numb_list:
        if (num != 0):
            result = num * result
    return result


###################################################
def number_base(str_number, radix):
    res = 0
    try:
        res = int(str_number, radix)
    except ValueError:
        res = -1
    return res


#################################################
def absolute_sorting(numbers_array):
    pre_arr = list(numbers_array)
    return list(sorted(pre_arr, key=abs))


###########################################:######
def non_inique_elements(data):
    list_data = list(data)
    for i in data:
        if (list_data.count(i) == 1):
            list_data.remove(i)
    return list_data


###################################################
def roman_numerals(data):
    # print(list(''.join(str(data))))
    result = []
    mille = int(data) // 1000
    # print(mille)
    quingenti = (data - mille * 1000) // 500
    # print(quingenti)
    centrum = (data - mille * 1000 - quingenti * 500) // 100
    # print(centrum)
    quinquaginta = (data - mille * 1000 - quingenti * 500 - centrum * 100) // 50
    # print(quinquaginta)
    decem = (data - mille * 1000 - quingenti * 500 - centrum * 100 - quinquaginta * 50) // 10
    # print(decem)
    quinque = (data - mille * 1000 - quingenti * 500 - centrum * 100 - quinquaginta * 50 - decem * 10) // 5
    # print(quinque)
    unus = (data - mille * 1000 - quingenti * 500 - centrum * 100 - quinquaginta * 50 - decem * 10 - quinque * 5) // 1
    # print(unus)
    result.append('M' * mille)

    if (quingenti + centrum == 5):
        result.append('CM')
    elif (quingenti + centrum == 4 and quingenti != 1):
        result.append('CD')
    else:
        result.append('D' * quingenti)
        result.append('C' * centrum)

    if (quinquaginta + decem == 5):
        result.append('XC')
    elif (quinquaginta + decem == 4 and quinquaginta != 1):
        result.append('XL')
    else:
        result.append('L' * quinquaginta)
        result.append('X' * decem)

    if (quinque + unus == 5):
        result.append('IX')
    elif (quinque + unus == 4 and quinque != 1):
        result.append('IV')
    else:
        result.append('V' * quinque)
        result.append('I' * unus)
    return str(''.join(result))


####################################################################
def cipher_map(cipher_grille, ciphered_password):
    # print(list(cipher_grille[1]).index('X'))
    # print(list(''.join(cipher_grille)))
    decode_message = []
    position = find_X(cipher_grille)
    decode_message.append(take_four_elem(position, ciphered_password))
    grille = cipher_grille
    for rot in range(3):
        grille = rotate_grille_90(grille)
        position = find_X(grille)
        decode_message.append(take_four_elem(position, ciphered_password))
    preconv_message = []
    for i in range(4):
        preconv_message.append(''.join(decode_message[i]))
    converted = (''.join(preconv_message))
    return converted


def find_X(array):
    finded_x = []
    for x in range(4):
        for y in range(4):
            if array[x][y] == 'X':
                finded_x.append([x, y])
    return list(finded_x)


def rotate_grille_90(grille):
    return list(zip(*grille[::-1]))


def take_four_elem(position, message):
    four_elem = []
    for i in range(4):
        four_elem.append(message[position[i][0]][position[i][1]])
    return four_elem


# print(cipher_map(
#    ('X...',
#     '..X.',
#     'X..X',
#     '....'),
#    ('itdf',
#     'gdce',
#     'aton',
#     'qrdi')
# ))

#####################################################################################################
def safe_pawns(pawns):
    save_counter = 0
    pawns_list = list(pawns)
    # print(pawns_list)
    result = 0
    # chessBoard = [[ i+1 for i in range(8)] for i in range(8)]
    # print(chessBoard)

    for pos in pawns_list:
        savers = calc_saver(pos)
        if (pawns.__contains__(savers[0]) or pawns.__contains__(savers[1])):
            save_counter += 1
    return save_counter


def calc_saver(position):
    savers = []
    if (position[1] == '1'):
        savers = calc_column_index(position)

    elif (position[1] == '2'):
        savers = calc_column_index(position)

    elif (position[1] == '3'):
        savers = calc_column_index(position)

    elif (position[1] == '4'):
        savers = calc_column_index(position)

    elif (position[1] == '5'):
        savers = calc_column_index(position)

    elif (position[1] == '6'):
        savers = calc_column_index(position)

    elif (position[1] == '7'):
        savers = calc_column_index(position)

    elif (position[1] == '8'):
        savers = calc_column_index(position)
    return savers


def calc_column_index(position):
    saver1 = None
    saver2 = None
    if (position[0] == 'a'):
        saver1 = 0
        saver2 = 'b' + str(int(position[1]) - 1)
    elif (position[0] == 'b'):
        saver1 = 'a' + str(int(position[1]) - 1)
        saver2 = 'c' + str(int(position[1]) - 1)
    elif (position[0] == 'c'):
        saver1 = 'b' + str(int(position[1]) - 1)
        saver2 = 'd' + str(int(position[1]) - 1)
    elif (position[0] == 'd'):
        saver1 = 'c' + str(int(position[1]) - 1)
        saver2 = 'e' + str(int(position[1]) - 1)
    elif (position[0] == 'e'):
        saver1 = 'd' + str(int(position[1]) - 1)
        saver2 = 'f' + str(int(position[1]) - 1)
    elif (position[0] == 'f'):
        saver1 = 'e' + str(int(position[1]) - 1)
        saver2 = 'g' + str(int(position[1]) - 1)
    elif (position[0] == 'g'):
        saver1 = 'f' + str(int(position[1]) - 1)
        saver2 = 'h' + str(int(position[1]) - 1)
    elif (position[0] == 'h'):
        saver1 = 'g' + str(int(position[1]) - 1)
        saver2 = 0
    return saver1, saver2


# print(calc_column_index('b3'))
#print(safe_pawns(["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"]))
