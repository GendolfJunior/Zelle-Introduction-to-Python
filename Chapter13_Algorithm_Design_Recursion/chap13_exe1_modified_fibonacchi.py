# 1. Modify the recursive Fibonacci program given in this chapter so that it prints tracing information. Specifically,
# have the function print a message when it is called and when it returns. For example, the output should
# contain lines like these:
#           Computing fib(4)
#           0 0 0
#           Leaving fib(4) returning 3
# Use your modified version of fib to compute fib(10) and count how many times fib(3) is computed in the process.

def recFib(n):
    # returns nth Fibonacci number
    # Note: this algorithm is exceedingly inefficient!
    print("computing fib({0})".format(n))
    if n < 3:
        return 1
    else:
        return recFib(n - 1) + recFib(n - 2)

import time

start_time = time.time()

def main():
    # data = [1, 2, 5, 1, 3]
    x = 910013733
    print(recFib(x))


main()
print("%s seconds" % (time.time() - start_time))
