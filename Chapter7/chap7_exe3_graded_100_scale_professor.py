# 3. A certain CS professor gives 100-point exams that are graded on the scale
# 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts
# an exam score as input and uses a decision structure to calculate the
# corresponding grade.

def main():
    score = int(input("Enter your exam score 0 - 100 range? "))
    if (score > 100 or score < 0):
        print("Score must be in a range of 0 to 100")
    else:
        if score < 60:
            print("You grade is F!")

        elif score < 70:
            print("You grade is D!")

        elif score < 80:
            print("You grade is C!")

        elif score < 90:
            print("You grade is B!")

        else:
            print("You grade is A!")


main()
