def addInterest(balance, rate):
    newbalance = balance * (1 + rate)
    return newbalance


def test():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount, rate)
    print(amount)
    #print(addInterest(amount, rate))


test()
