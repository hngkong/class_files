# Define a class MyStudent with attributes:
# fname, lname, type = "Grad", semesterAttended = 1
# There is one method - studentData() - that will combine the
# values of attributes into a string.

# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: None, in class work
# Software/Program Reference Number: Student Objects
# Software/Program Brief Description: Create a student class object
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/02/04     First Version
# *********************************************************************************************************
# Variable Initialization

class MyStudent():
    
    # create object variables
    fname = ""
    lname = ""
    type = "Grad"
    semesterAttended = 1
    dataStr = ""

    # create object methods
    def studentData(self):
        dataStr = "%s %s is a %s student and he/she has completed %s semesters." % (self.fname, self.lname, self.type, self.semesterAttended)
        print(dataStr)


def main():

    # instantiate the student object
    person = MyStudent()

    # print default values
    person.studentData()

    print("The student's first name is", person.fname, "\nThe student's last name is", person.lname)
    
    person.fname = "John"
    person.lname = "Doe"

    print("The student's first name is", person.fname, "\nThe student's last name is", person.lname)
        
    # do stuff?
    person.studentData()

main()