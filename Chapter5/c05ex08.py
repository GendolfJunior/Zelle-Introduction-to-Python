# c05ex08.py
#    Caesar cipher (circular version)


def main():
    print("Caesar cipher")
    print()

    key = int(input("Enter the key value: "))
    plain = input("Enter the phrase to encode: ")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    print("the len(chars) is: ", len(chars))

    cipher = ""
    for letter in plain:

        print("current letter is: ", letter)
        pos = chars.find(letter)
        print("current pos is: ", pos)
        newpos = (pos + key) % len(chars)
        print("current newpos is: ", newpos)
        cipher = cipher + chars[newpos]
        print("current cipher is: ", cipher)

    print("Encoded message follows:")
    print(cipher)


main()
