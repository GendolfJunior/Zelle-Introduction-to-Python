# Exercise 1
# Many companies pay time-and-a-half for any hours worked above 40 in a
# given week. Write a program to input the number of hours worked and
# the hourly rate and calculate the total wages for the week.

def main():
    hoursWorked = int(input("Enter how many hours you worked? "))
    hourlyRate = int(input("Enter your rate? "))
    totalEarnings = 0.0
    if hoursWorked <= 40:
        totalEarnings = hoursWorked * hourlyRate
        print("The total earnings are", totalEarnings)
    else:
        overtime = (hoursWorked - 40) * hourlyRate * 1.5
        normalPay = 40 * hourlyRate
        totalEarnings = normalPay + overtime
        print("The total earnings are", totalEarnings)
        print("inclduing overtime", overtime)

if __name__ == '__main__':
    main()