# 8. A person is eligible to be a US senator if they are at least 30 years old
# and have been a US citizen for at least 9 years. To be a US representative
# these numbers are 25 and 7, respectively. Write a program that accepts a
# person's age and years of citizenship as input and outputs their eligibility
# for the Senate and House.

# input: age, citizenship years
# output: US sentator eligibility, US representative eligibility

def main():
    age = int(input("Enter your age (full years): "))
    citizenship_years = int(input("Enter how many years you've been a US citizen: "))
    senator_eligible = "not eligible"
    representation_eligible = "not eligible"
    if (age > 29 and citizenship_years > 8):
        senator_eligible = 'eligible'
    if (age > 24 and citizenship_years > 6):
        representation_eligible = 'eligible'

    print("You are {0} to be US senator,\nand you are {1} to be US representative".format(senator_eligible, representation_eligible))

if __name__ == '__main__':
    main()