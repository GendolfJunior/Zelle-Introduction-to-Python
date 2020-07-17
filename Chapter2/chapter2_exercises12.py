# Write an interactive Python calculator program. The program should allow
# the user to type a mathematical expression, and then print the value of the
# expression. Include a loop so that the user can perform many calculations
# (say, up to 100). Note: To quit early, the user can make the program
# crash by typing a bad expression or simply closing the window that the
# calculator program is running in. You'll learn better ways of terminating
# interactive programs in later chapters.

# specification:
# main function where
# user is prompted to input mathematical expression
# an expression is evaluated by the program
# program prints out the result
# program starts all over and prompts user to input mathematical expression
# call out the main function

def main():
    for i in range(100):
        mathExpresssion = eval(input("Enter mathematical expression, like 222 / 11, 33 * 3, etc: "))
        print("the result is:", mathExpresssion)


main()
