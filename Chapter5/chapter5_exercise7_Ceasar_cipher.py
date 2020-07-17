# A Caesar cipher is a simple substitution cipher based on the idea of shifting each letter of the plaintext message a fixed number (called the key) of
# positions in the alphabet. For example, if the key value is 2, the word "Sourpuss" would be encoded as "Uqwtrwuu." The original message can
# be recovered by "reencoding" it using the negative of the key Write a program that can encode and decode Caesar ciphers. The input
# to the program will be a string of plaintext and the value of the key. The output will be an encoded message where each character in the original
# message is replaced by shifting it key characters in the Unicode character set. For example, if ch is a character in the string and key is the
# amount to shift, then the character that replaces ch can be calculated as: chr (ord (ch) + key).

# get input of text string
# get input of the key
# encode the string using a formula chr(ord(ch) + key)
# print out the encoded string

def main():
    text = input("Enter the text to encrypt: ")
    encryptionKey = int(input("Enter the key: "))
    enc_message = []
    for numStr in text:
        enc_message.append(chr(ord(numStr) + encryptionKey))
        print("current enc message is: ", enc_message)

    final_message = "".join(enc_message)
    print("The encrypted message is: ", final_message)


main()
