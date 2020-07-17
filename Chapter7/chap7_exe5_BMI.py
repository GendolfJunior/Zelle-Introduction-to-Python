# 5. The body mass index (BMI) is calculated as a person's weight (in pounds)
# times 720, divided by the square of the person's height (in inches). A BMI
# in the range 19-25, inclusive, is considered healthy. Write a program that
# calculates a person's BMI and prints a message telling whether they are
# above, within, or below the healthy range.

# Inputs: weight and height as float
# output: your BMI and is it above, within, or below the healthy range.

# Algorithm
# bmi = (weight * 720) / height
# if statement

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    bmi = (weight * 720) / height ** 2
    bmi_message = ''
    if (19 < bmi < 25):
        bmi_message = 'your bmi is within the healthy range'
    elif bmi < 19:
        bmi_message = 'your bmi is below the healthy range'
    else:
        bmi_message = 'your bmi is above the healthy range'
    print(bmi, " - ", bmi_message)


if __name__ == '__main__':
    main()
