# 2. Extend the gpasort program so that it allows the user to sort a file of
# students based on GPA, name, or credits. Your program should prompt for
# the input file, the field to sort on, and the output file.

# gpasort.py
#   A program to sort student information into GPA order

from Chapter11_Data_Collections.gpa import Student, makeStudent


def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students


def writeStudents(students, filename):
    # students is a list of Student object
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints(), s.gpa()), file=outfile)
    outfile.close()


def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file to read from: ")
    sorting = input("Enter the field to be used for sorting. Options: gpa, name, or credits: ")

    data = readStudents(filename)
    if sorting == 'gpa':
        data.sort(key=Student.gpa)
    elif sorting == 'name':
        data.sort(key=Student.getName)
    else:
        data.sort(key=Student.getHours)
    filename = input("enter a name for the outputfile: ")
    writeStudents(data, filename)
    print("the data has been written to", filename)


if __name__ == '__main__': main()
