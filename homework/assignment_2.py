# *********************************************************************************************************
# Class: CSIT 512
# Author: Charles Kline
# Due Date: 2019/01/28
# Software/Program Reference Number: Assignment 2
# Software/Program Brief Description: Input the number of people, loop number of people times,
#                                     then input the education years for each.  Display the
#                                     education level, then at the end, display total people,
#                                     education years, and average education years.
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ==========     ===========
# 1.0        CK              2019/01/28     Initial release
# *********************************************************************************************************
# Variable Initialization
#
totalYears: int = 0
x: int = 0
# Step 1 (I) – Request total number of people
numPeople = int(input("Please input number of people to be entered: "))
# Step 2 (P) – Loop total number of people times
for x in range(1, numPeople+1):
    # Step 3 (I) – Request education years
    prompt = "Please enter the total number of education years for person " + str(x) + ": "
    edYears = int(input(prompt))
    # Step 4 (O) – Use if else if statement to output what level of education they have
    totalYears += edYears
    # Step 5 (P) – Add input education years to total years
    if edYears < 12:
        print("Person", x, "does not have a degree.")
    elif 12 <= edYears < 16:
        print("Person", x, "has a high school diploma.")
    elif 16 <= edYears < 18:
        print("Person", x, "has a bachelor's degree.")
    elif 18 <= edYears < 23:
        print("Person", x, "has a master's degree.")
    elif edYears >= 23:
        print("Person", x, "has a PhD.")
# Step 6 (P) – Average the education years by total people
aveYears = float(totalYears / numPeople)
# Step 7 (O) – Output total people, total education years, and average education years
print("There were", numPeople, "people entered")
print("The total years of education they have is:", totalYears)
print("The average number of years of education is:", aveYears)
