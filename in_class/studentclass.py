# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: None, in class work
# Software/Program Reference Number: Objects Class
# Software/Program Brief Description: Create a student class object
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/02/04     First Version
# *********************************************************************************************************
# Variable Initialization

class Student():
    
    # create object variables
    name = "John Doe"

    # create object methods
    def example(self):
        print("example")


def main():

    # instantiate the student object
    person = Student()

    # do stuff?
    person.example()

main()