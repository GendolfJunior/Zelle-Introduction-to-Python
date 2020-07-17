# 16. A Fibnoacci sequence is a sequence of numbers where each successive number is the sum of the previous two. The classic Fibonacii sequence
#     begins: 1, 1, 2, 3, 5, 8, 13 ... . Write a program that computes the nth Fibonacci number where n is a value input by the user. For example,
#     if n = 6, then the result is 8.

# prompt user input of the n-th value
# starting number is 1

def main():
    n = int(input("Enter n-th Fibonachi number: "))
    cur, prev = 1, 1
    for i in range(n - 2):
        cur, prev = cur + prev, cur

        print("loop", str(cur), str(prev))

    print()
    print("The nth Fibonacci number is: ", cur)


main()
