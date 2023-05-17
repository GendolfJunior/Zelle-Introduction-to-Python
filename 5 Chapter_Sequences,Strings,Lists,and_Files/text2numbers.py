# text2numbers . py
# A program to convert a textual message into a sequence of
# numbers , ut ilizing the underlying Unicode encoding .
def main():
    print(" This program converts a textual message into a sequence ")
    print(" of numbers representing the Unicode encoding of the message . \n")
    # Get the message to encode
    message = input(" Please enter the message to encode : ")
    print("\nHere are the Unicode codes: ")
    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")
        #print()  # blank l ine before prompt


main()
