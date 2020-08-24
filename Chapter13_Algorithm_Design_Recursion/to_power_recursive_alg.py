def recPower(a, n):
    # raises a to the int power n
    if n == 0:
        return 1
    else:
        factor = recPower(a, n // 2)
        if n % 2 == 0:  # n is even
            return factor * factor
        else:  # n is odd
            return factor * factor * a
