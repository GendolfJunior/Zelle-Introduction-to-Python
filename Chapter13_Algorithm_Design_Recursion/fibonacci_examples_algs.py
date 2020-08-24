def loopfib(n):
    # returns the nth Fibonacc i number
    curr = 1
    prev = 1
    for i in range(n - 2):
        curr, prev


def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
