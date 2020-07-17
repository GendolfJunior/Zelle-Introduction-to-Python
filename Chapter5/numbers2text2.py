# numbers2text2.py
# A program to convert a sequence of Unicode numbers into
# a string of text. Efficient version using a list accumulator.
# sample message 83 116 114 105 110 103 115 32 97 114 101 32 70 117 110 33

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents. \n")

    # Get the message to encode
    inString = input(" Please enter the Unicode-encoded message : ")

    # Loop through each substring and build Unicode message
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr)           # convert digits to a number
        chars.append(chr(codeNum))      # accumulate new character

    message = "".join(chars)
    print("\n The decoded message is: ", message)


main()
