#  2. Write a program to print the lyrics for ten verses of "The Ants Go Marching." A couple of sample versus are given below.
#     You may choose your own activity for the "little one" in each verse, but be sure to choose something that makes the rhyme
#     work (or almost work).

def go_marching():
    num = "And they all go marching down...\nIn the ground...\nTo get out...\nOf the rain.\n" + ("Boom! " * 3)
    return num

def hurarah(number):
    hur = " hurrah!" * 2 + "\n"
    line = ("The ants go marching " + number + " by " + number)
    line2 = line + hur
    print(line2 * 2 + line)

def little(action):
    print("The little one stops to", action)

def main():
    numbers = [("one", "suck his thumb"), ("two", "tie his shoe"), ("three", "suck the tits")]
    for a, n in numbers:
        hurarah(a)
        little(n)
        print(go_marching())

main()