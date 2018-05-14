MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    # replace this for solution

    words = get_morse_word_with_let(code)
    print(words)
    msg = ""
    for word in words:
        msg+="1"
        for let in word:
            if let is "":
                continue
            msg += MORSE[let]
    print(msg)
    return msg.capitalize()


def get_morse_word_with_let(code):
    splitted_word = code.split(" ")
    res = []
    for word in splitted_word:
        res.append(str(word).split(" "))
    return res


if __name__ == '__main__':
    print("Example:")
    # print(morse_decoder('... --- ...'))
    print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))

    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert morse_decoder("... --- -- .  - . -..- -") == "Some text"
    # assert morse_decoder("..--- ----- .---- ---..") == "2018"
    # assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    # print("Coding complete? Click 'Check' to earn cool rewards!")
