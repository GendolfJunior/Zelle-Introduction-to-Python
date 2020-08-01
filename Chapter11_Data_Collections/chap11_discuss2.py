# a) s1.remove(2)               - removes 2
# b) s1.sort()                  - sorts [1,2,3,4]
# c) s1.append([s2.index('b')]) - [2,1,4,3,2]
# d) s2.pop(s1.pop(2))          - ["c", "a", "b"]
# e) s2.insert(s1[0], "d")      - ["c", "a", "d", "b"]

def aaa(s1, x):
    s1.remove(x)
    return s1


def bbb(s1):
    s1.sort()
    return s1


def ccc(s1, s2):
    s1.append(s2.index("b"))
    return s1


def ddd(s1, s2):
    s2.pop(s1.pop(2))
    return s2


def eee(s1, s2):
    s2.insert(s1[0], "d")
    return s2


def main():
    s1 = [2, 1, 4, 3]
    s2 = ["c", "a", "b"]
    #  print(aaa(s1, 2))
    #  print(bbb(s1))
    #  print(ccc(s1, s2))
    #  print(ddd(s1, s2))
    print(eee(s1, s2))


main()
