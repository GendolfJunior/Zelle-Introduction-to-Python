# 2

class FibCounter:

    def __init__(self):
        self.count = 0

    def getCount(self):
        return self.count

    def resetCount(self):
        self.count = 0

    def recFib(self, n):
        # returns nth Fibonacci number
        # Note: this algorithm is exceedingly inefficient!
        self.count = self.count + 1
        if n < 3:
            return 1
        else:
            result = self.recFib(n - 1) + self.recFib(n - 2)
            return result


def main():
    print()
    print("Let's count the recursive calls for Fibonacci numbers!")
    print()

    FC = FibCounter()

    n = int(input("Computing the n-th Fibonacci number. Enter n.: "))

    answer = FC.recFib(n)
    count = FC.getCount()

    print()
    print("Fib({0}) is {1} and used {2} function calls.".format(n, answer, count))
    print()


main()
