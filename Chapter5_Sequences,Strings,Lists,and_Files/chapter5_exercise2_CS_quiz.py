# A certain CS professor gives 5-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as
# an input and prints out the corresponding grade.

# print the intro
# take input from the use in variable and give instruction what variables are eligible
# create a for list of grades
# create a for score in range of the list of grades
# print what is the grade

def main():
    print("this programs take your score value and returns your grade")
    score = int(input("Enter your score as an integer: "))
    grade = ["F", "F", "D", "C", "B", "A"]
    yougrade = grade[score]
    print("your grade my friend is: ", yougrade)


main()
