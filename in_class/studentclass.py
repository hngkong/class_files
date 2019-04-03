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
    fname = "John"
    lname = "Doe"
    type = "Grad"
    semesterAttended = 1
    finishedString = "Nothing"

    # create object methods
    def studentData(self):
        finishedString = fname + lname + str(type) + semesterAttended
        print(finishedString)


def main():

    # instantiate the student object
    person = MyStudent()

    # do stuff?
    person.studentData()

main()