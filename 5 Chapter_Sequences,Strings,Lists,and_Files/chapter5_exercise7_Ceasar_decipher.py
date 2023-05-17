# get input of text string
# get input of the key
# decode the string using a formula chr(ord(ch) - key)
# print out the encoded string

def main():
    text = input("Enter the text to encrypt: ")
    encryptionKey = int(input("Enter the key: "))
    enc_message = []
    for numStr in text:
        enc_message.append(chr(ord(numStr) - encryptionKey))
       # print("current enc message is: ", enc_message)

    final_message = "".join(enc_message)
    print("The encrypted message is: ", final_message)


main()
