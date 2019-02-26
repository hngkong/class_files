# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date:
# Software/Program Reference Number: Homework Assignment 3
# Software/Program Brief Description: Write a project that has three functions
#                                     that take input and return the values
#                                     before printing to the console.
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/19/02     First Version
# *********************************************************************************************************
# Variable Initialization


# Step 1: Define get_Fname function
def get_Fname():
    # Step 1.1: Get the first_name value through input
    first_name = input("Please enter your first name: ")
    # Step 1.2: Return first_name value
    return first_name

# Step 2: Define get_Lname function
def get_Lname():
    # Step 2.1: Get the last_name value through input
    last_name = input("Please enter your last name: ")
    # Step 2.2: Return last_name value
    return  last_name

# Step 3: Define Get_Age function
def get_Age():
    # Step 3.1: Get the age value through input
    age = input("Please enter your age: ")
    # Step 3.2: Return age value
    return age

# Step 4: Define prin_Data function
def prin_Data(f_name, l_name, p_age):
    # Step 4.1: Take three parameters: f_name, l_name, and p_age(parameter_age)
    #           and use them in the print command
    print("Hi " + f_name + " " + l_name + ", your age is " + p_age + ".")

# Step 5: Define main function
def main():
    # Step 5.1: Call the prin_Data method with 3 methods as the parameters
    prin_Data(get_Fname(),get_Lname(),get_Age())

# Step 6: Call main()
main()