# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: 3/12/2019
# Software/Program Reference Number: Midterm Part 2
# Software/Program Brief Description: Write a project that calculates
#                                     circumference and radius of a circle
#                                     and prints them to the console.
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/12/03     First Version
# *********************************************************************************************************
# Variable Initialization

# Step 1: Import math
import math


# Step 2: Define main() function
def main():
    # Step 2: Input radius and set to variable r
    r = int(input("Please input radius: "))
    # Step 3: Call prin_data(r)
    prin_data(r)


def prin_data(r):
    # Step 3a: Print “The area of the circle is” find_area(r) “and the circumference is” find_circumference(r)
    print("The area of the circle is", find_area(r), "and the circumference is", find_circumference(r))


# Step 4: Call find_area(r)
def find_area(r):
    # Step 4a: Return pi*(r*r)
    return math.pi * (r * r)


# Step 5: Call find_circumference(r)
def find_circumference(r):
    # Step 5a: Return 2 * math.pi * r
    return 2 * math.pi * r


# Step 6: Call main()
main()


example
