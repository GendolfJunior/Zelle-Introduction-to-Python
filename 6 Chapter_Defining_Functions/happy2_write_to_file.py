# happy2.py
def happy():
    return "Happy Birthday to you!\n"


def verseFor(person):
    lyrics = happy() * 2 + "Happy birthday, dear " + person + ".\n" + happy()
    return lyrics


def main():
    outf = open("Happy_birthday.txt", "w")
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verseFor(person), file=outf)
    outf.close()


main()
