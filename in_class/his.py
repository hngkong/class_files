# Define a class MyClass with one attribute myVar, and one method myOps.  This method
# simply prints "This is the method myOps".  Display the value of the attribute myVar.
# Then change the value of the attribute to "Passed"
# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: 3/12/2019
# Software/Program Reference Number: Objects Class
# Software/Program Brief Description: Objects/Classes
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/26/03     First Version
# *********************************************************************************************************
# Variable Initialization

class MyClass:

    # define variable
    myVar = "test"

    # define myOps()
    def myOps(self):
        print("This is the method myOps")
        print(self.myVar)

def main():
    example = MyClass()

    example.myOps()

    example.myVar = "Passed"

    example.myOps()

main()