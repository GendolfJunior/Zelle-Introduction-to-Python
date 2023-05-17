# input number to take factorial of, n
# compute factorial of n, fact
    # initalize the accumulator variable
    # loop until final result is reached
    # update the value of accumulator variable
# output fact

factorial = int(input("Enter a number for factorial of: "))
fact = 1
for i in range(1, factorial + 1, 1):
    fact = i * fact
    print("fact is: ", fact)

print("---------------------------------------------------")
print("Another version")

factorial = int(input("Enter a number for factorial of: "))
fact = 1
for i in range(factorial, 1, -1):
    fact = i * fact
    print("fact is: ", fact)
