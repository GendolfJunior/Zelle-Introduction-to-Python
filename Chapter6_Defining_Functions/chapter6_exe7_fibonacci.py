# 7. write a function to compute the nth Fibonacci number. Use your function to solve Programming Exercise 16 from Chapter 3.
# A Fibnoacci sequence is a sequence of numbers where each successive number is the sum of the previous two. The classic Fibonacii sequence
#     begins: 1, 1, 2, 3, 5, 8, 13 ...

# prompt user input of the n-th value
# starting number is 1

def fibo(n):
    cur, prev = 1, 1
    for i in range(n - 2):
        print(i)
        cur, prev = cur + prev, cur
        print(cur, prev)
    return cur


def main():
    n = int(input("Enter n-th Fibonachi number: "))
    print()
    print("The nth Fibonacci number is: ", fibo(n))


main()
