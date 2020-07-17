def sumDiff(x, y):
    sum = x + y
    diff = x - y
    return sum, diff

num1, num2 = input("Please enter two numbers (num1, num2: ) ").split(",")
s, d = sumDiff(float(num1), float(num2))
print("The sum is", s, "and the difference is", d)