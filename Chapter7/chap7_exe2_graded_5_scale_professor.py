# 2. A certain CS professor gives five-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an
# input and uses a decision structure to calculate the corresponding grade.

def main():
    score = int(input("Enter your quiz score? "))
    if score > 5:
        print("Score must be in a range of 0 to 5")
    else:
        if score == 5:
            print("You grade is A!")

        elif score == 4:
            print("You grade is B!")

        elif score == 3:
            print("You grade is C!")

        elif score == 2:
            print("You grade is D!")

        else:
            print("You grade is F!")


main()
