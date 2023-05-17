# 1 . The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, . . .. Each number in the sequence
# (after the first two) is the sum of the previous two. Write a program
# that computes and outputs the nth Fibonacci number, where n is a
# value entered by the user.

def fibo(n):
    cur, prev = 1, 1
    i = 0
    while i < (n - 2):
        cur, prev = cur + prev, cur
        print(cur, prev)
        i += 1
    return cur


def main():
    n = int(input("Enter n-th Fibonachi number: "))
    print()
    print("The nth Fibonacci number is: ", fibo(n))


if __name__ == '__main__':
    main()
