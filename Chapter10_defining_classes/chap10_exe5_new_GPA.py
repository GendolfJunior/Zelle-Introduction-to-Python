# 5. Modify the Student class from the chapter by adding a mutator method
# that records a grade for the student. Here is the specification of the new
# method:
#           addGrade(self, gradePoint, credits) gradePoint is a float that represents
#                   a grade (e.g., A = 4.0, A- = 3.7, B+ = 3.3, etc.), and credits
#                   is a float indicating the number of credit hours for the class. Modify
#                   the student object by adding this grade information.
# Use the updated class to implement a simple program for calculating GPA.
# Your program should create a new student object that has 0 credits and 0
# quality points (the name is irrelevant). Your program should then prompt
# the user to enter course information (gradePoint and credits) for a series
# of courses, and then print out the final GPA achieved.

# page 328 program to find student with the highest GPA


class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        self.qpoints = self.qpoints + gradePoint * credits
        self.hours = self.hours + credits


def main():
    print("This program computes a student's GPA")
    student = Student("No Name", 0, 0)

    infoStr = input("Enter course info (gradepoints, credits): ")
    while infoStr != "":
        data = infoStr.split(",")
        gp, credits = float(data[0]), float(data[1])
        student.addGrade(gp, credits)
        infoStr = input("Enter course info (gradepoints, credits): ")

    print("\nSummary of courses entered:")
    print("hours:", student.getHours())
    print("GPA:", student.gpa())


if __name__ == '__main__':
    main()
