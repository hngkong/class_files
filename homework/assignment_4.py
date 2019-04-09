# *********************************************************************************************************
# Class: IT-512 Spring 2019
# Author: Charles Kline
# Due Date:
# Software/Program Reference Number: Homework Assignment 4
# Software/Program Brief Description: The program should ask for a file name 
#                                     and display the data in the file, before
#                                     calculating the total of the date, then
#                                     calculating the average of the data
#
# Ver No.    Name(Initials)  Date           Description
# =======    ==============  ===========    ===========
# 1.0        CK              2019/08/04     First Version
# *********************************************************************************************************
# Variable Initialization

def main():

    data_total = 0
    data_average = 0
    total_lines = 0

    # 1. Ask the user for the file name
    file_name = str(input("What is the name of the file you want to use:"))


    # 2. Load the file
    data = open(file_name, 'r')
    # 2.5. Read the data from the file
    for line in data:
        number = float(data)
        # 3. Display the contents of the file
        print("Line {}: {}".format(line, number))
        data_total = data_total + data
        total_lines = line

    # 4. Display the total of all the data
    print("The total sum of the data is:", data_total)
    
    # 5. Display the average of all the data
    data_average = data_total/total_lines
    print("The average of the data is:", data_average)
    
main()