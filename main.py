from index import convert_dict


def convert():
    morse = ""
    a = input("Please enter what you wish to code into morse: ")

    for char in a.lower():
        morse += convert_dict[char]

    print(morse)


convert()
