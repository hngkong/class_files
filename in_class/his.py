# Define a class MyClass with one attribute myVar, and one method myOps.  This method
# simply prints "This is the method myOps".  Display the value of the attribute myVar.
# Then change the value of the attribute to "Passed"
# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: None, in class work
# Software/Program Reference Number: Objects Class
# Software/Program Brief Description: Objects/Classes practice
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/02/04     First Version
# *********************************************************************************************************
# Variable Initialization

class MyClass:

    # define variable
    myVar = "test"

    # define myOps()
    def myOps(self):
        print("This is the method myOps")

def main():

    # instantiate an object of MyClass()
    example = MyClass()

    # print the default value of the attribute myVar
    print(example.myVar)

    # assign a new value to myVar
    example.myVar = "Passed"

    # print the updated value of myVar
    print(example.myVar)

    # call the method myOps() of the class MyClass() 
    example.myOps()

main()