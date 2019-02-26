# *********************************************************************************************************
# Class: CSIT 512
# Author: Charles Kline
# Due Date: 2019/01/22
# Software/Program Reference Number: Assignment 1
# Software/Program Brief Description: Take the input of three numbers, sum them and print
#
#
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ==========     ===========
# 1.0        CK              2019/01/22     Initial release
# *********************************************************************************************************
# Variable Initialization
#
# Step 1 (I) – Request the first number input
firstNum = int(input("Please enter the first number: "))
# Step 2 (I) – Request the second number input
secondNum = int(input("Please enter the second number: "))
# Step 3 (I) – Request the third number input
thirdNum = int(input("Please enter the third number: "))
# Step 4 (P) – Sum the three input numbers
numSum = firstNum+secondNum+thirdNum
# Step 5 (O) – Print the sum to the console
print("The sum of the three numbers is", numSum)

