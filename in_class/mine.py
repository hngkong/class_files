# Define a class MyClass with one attribute myVar, and one method myOps.  This method
# simply prints "This is the method myOps".

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

    def __init__(self):
        self.myVar = "This is the method myOps"

    def myOps(self):
        print(self.myVar)

def main():
    example = MyClass()
    example.myOps()

main()