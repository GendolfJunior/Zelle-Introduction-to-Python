#  3. A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
#     Write a program that accepts an exam score as input and prints out the corresponding grade.

def main():
    score = int(input("Enter the student score as an integer: "))
    grades = "F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A" * 11
    yourGrade = grades[score]
    print("You score is {0} and your grade is {1}".format(score, yourGrade))

main()
