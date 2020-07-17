# eval() is used when you expect number to be inputed rather than text literal
# eval is very dangerous functions and could be exploited by hackers. It is called CODE INJECTION attackes
# because it will evaluate whatever command is supplied like send me this or that or delete these files, etc.

ans = eval(input("Enter an expression: "))
#like 3 + 4 * 5

print(ans)
# the output with 3 + 4 * 5  is going to yield 23 because eval() evaluated the mathematical expression 3 + 4 * 5