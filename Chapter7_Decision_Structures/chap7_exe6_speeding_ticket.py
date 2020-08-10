# 6. The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph
# over the limit plus a penalty of $200 for any speed over 90 mph. Write a
# program that accepts a speed limit and a clocked speed and either prints
# a message indicating the speed was legal or prints the amount of the fine,
# if the speed is illegal.

# inputs: 1) speed limit and 2) clocked speed
# output: 1) message whether your speed was legal or illegal

# algorithm

def main():
    limit = float(input("Enter the speed limit: "))
    clocked_speed = float(input("Enter what was actual speed recorded: "))
    penalty = 0.0
    if clocked_speed > limit:
        penalty = (clocked_speed - limit) * 5 + 50
        if clocked_speed >= 90:
            penalty += 200
        print("the speed was illegal and your fine is ", penalty)
    elif clocked_speed >= 90:
            penalty += 200
            print("the speed was illegal and your fine is ", penalty)
    else:
        print("the speed was legal")


if __name__ == '__main__':
    main()
