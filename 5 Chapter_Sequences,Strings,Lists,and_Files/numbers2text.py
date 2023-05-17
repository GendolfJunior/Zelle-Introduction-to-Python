# numbers2text.py
# A program to convert a sequence of Unicode numbers into a string of text.
# sample message 83 116 114 105 110 103 115 32 97 114 101 32 70 117 110 33

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents. \n")

    # Get the message to encode
    inString = input(" Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    message = " "
    for numstr in inString.split():
        print("the numstr is: ", numstr)
        codeNum = int(numstr)                         # convert digits to a number
        #print("the codenum is: ", codeNum)
        message = message + chr(codeNum)              # concatentate character to message
    print("\nThe decoded message is : ", message)


main()