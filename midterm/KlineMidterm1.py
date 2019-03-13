# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date: 3/12/2019
# Software/Program Reference Number: Midterm Part 1
# Software/Program Brief Description: Write a project calculates the
#                                     calories burned for 3-8 miles
#                                     before printing to the console.
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/12/03     First Version
# *********************************************************************************************************
# Variable Initialization

#Step 1: Define main() function
def main():
#Step 2: initialize caloriesPerMile variable and set to 100
    caloriesPerMile = 100
#Step 3: Create for loop that loops 9 times
    for x in range(9):
#Step 4: If statement which checks if the loop is on iteration 3 or greater
        if x > 2:
#Step 5: If the if statement is true, multiply caloriesPerMile by loop iteration and assign to caloriesBurned
            caloriesBurned = x * caloriesPerMile
#Step 6: Print caloriesBurned to console
            print("After", x, "miles, you have burned", caloriesBurned, "calories.")
#Step 7: Repeat loop until finished

#Step 8: Call main()
main()