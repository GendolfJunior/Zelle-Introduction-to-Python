# this exercise demonstrates how usefull is simultaneous assignment
x = 2
y = 4
sum, diff = x + y, x - y

print("x y values: ", str(x), str(y))

x = y
print("x y values: ", str(x), str(y))
print("the sum is: ")
print(sum)
print("The diff is: ")
print(diff)