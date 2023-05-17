def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


def main():
    data = "Andriy"
    print(reverse(data))


if __name__ == '__main__':
    main()
